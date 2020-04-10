package main

import (
	"container/list"
	"strings"
)

/*
Parser
We define  a parser type that takes some parser
input and produces a parser result
*/
type Parser func(ParserInput) ParserResult

func (parser Parser) OrElse(alternativeParser Parser) Parser {
	return func(input ParserInput) ParserResult {
		var res1 = parser(input)

		if res1.Result != nil {
			return res1
		}

		return alternativeParser(input)
	}
}

// Map is equivalent to the haskell F a -> (a -> b) => F b
// this yields us something like Parser a -> (a -> b) => Parser b
// this allows us to transform the result conveniently for further processing
func (parser Parser) Map(mapFunc func(interface{}) interface{}) Parser {
	return func(input ParserInput) ParserResult {
		var res = parser(input)

		if res.Result != nil {
			return ParserResult{mapFunc(res.Result), res.RemainingInput}
		}

		return res
	}
}

// Bind is equivalent to M a -> (a -> M b) -> M b
func (parser Parser) Bind(bindF func(interface{}) Parser) Parser {
	return func(input ParserInput) ParserResult {
		var res = parser(input)
		var secondParser = bindF(res.Result)
		return secondParser(res.RemainingInput)
	}
}

// Left takes the left result from a pair parser
func (parser Parser) Left() Parser {
	return parser.Map(GetFirst)
}

// Right takes the right result from a pair parser
func (parser Parser) Right() Parser {
	return parser.Map(GetSecond)
}

type Pair struct {
	First  interface{}
	Second interface{}
}

func GetFirst(argument interface{}) interface{} {
	var pair, isPair = argument.(Pair)
	if isPair {
		return pair.First
	}

	return argument
}

func GetSecond(argument interface{}) interface{} {
	var pair, isPair = argument.(Pair)
	if isPair {
		return pair.Second
	}

	return argument
}

type Nothing struct{}

// Optional uses Maybe semantics where we return an empty struct
// if the parser failed to parse else we return the parsed result
func (parser Parser) Optional() Parser {
	return func(input ParserInput) ParserResult {
		var result = parser(input)

		if result.Result == nil {
			return ParserResult{Nothing{}, input}
		}

		return result
	}
}

// AndThen sequences the operations of two parsers such that the
// result contains a pair of results from each parser
func (parser Parser) AndThen(nextParser Parser) Parser {
	return func(input ParserInput) ParserResult {
		var res1 = parser(input)

		if res1.Result == nil {
			return ParserResult{nil, input}
		}

		var remInput = res1.RemainingInput
		var res2 = nextParser(remInput)

		if res2.Result == nil {
			return ParserResult{nil, remInput}
		}

		return ParserResult{Pair{res1.Result, res2.Result}, res2.RemainingInput}
	}
}

/*
ParserInput

A parser input comprises of the current code point
and the remaining stream to process
*/
type ParserInput interface {
	CurrentCodePoint() rune
	RemainingInput() ParserInput
}

/*
	A ParserResult
	comprises of the result we have built so
	far and remaining input
*/
type ParserResult struct {
	Result         interface{}
	RemainingInput ParserInput
}

// AnyChar consumes a single char from the stream
func AnyChar() Parser {
	return func(input ParserInput) ParserResult {
		return ParserResult{input.CurrentCodePoint(), input.RemainingInput()}
	}
}

// ExpectCodePoint creates a function that checks if
// the expected code point is created
func ExpectCodePoint(expectedCodePoint rune) Parser {
	return func(input ParserInput) ParserResult {
		if expectedCodePoint == input.CurrentCodePoint() {
			return ParserResult{expectedCodePoint, input.RemainingInput()}
		}
		return ParserResult{nil, input}
	}
}

// ExpectCodePoints creates a parser that expects a sequence of runes
// to be parsed
func ExpectCodePoints(expectedCodePoints []rune) Parser {
	return func(input ParserInput) ParserResult {
		var RemainingInput = input
		for _, codePoint := range expectedCodePoints {
			if nil == RemainingInput {
				return ParserResult{nil, RemainingInput}
			}

			var result = ExpectCodePoint(codePoint)(RemainingInput)

			if result.Result == nil {
				return ParserResult{nil, RemainingInput}
			}

			RemainingInput = result.RemainingInput
		}

		return ParserResult{expectedCodePoints, RemainingInput}
	}
}

func ExpectString(expectedString string) Parser {
	return func(input ParserInput) ParserResult {
		var result = ExpectCodePoints([]rune(expectedString))(input)

		var runes, isRuneArray = result.Result.([]rune)

		if isRuneArray {
			return ParserResult{string(runes), result.RemainingInput}
		}

		return result
	}
}

func Repeated(parser Parser) Parser {
	return func(input ParserInput) ParserResult {
		var parseList = list.New()
		var RemainingInput = input
		for RemainingInput != nil {
			var singleParseResult = parser(RemainingInput)
			RemainingInput = singleParseResult.RemainingInput
			if singleParseResult.Result != nil {
				parseList.PushBack(singleParseResult.Result)
			} else {
				break
			}
		}

		return ParserResult{parseList, RemainingInput}
	}
}

func OneOrMore(parser Parser) Parser {
	return func(input ParserInput) ParserResult {
		var result = Repeated(parser)(input)

		if result.Result.(*list.List).Len() > 0 {
			return result
		}

		return ParserResult{nil, input}
	}
}

func Satisfy(parser Parser, pred func(interface{}) bool) Parser {
	return func(input ParserInput) ParserResult {
		var res = parser(input)

		if res.Result != nil {
			if pred(res.Result) {
				return res
			}
		}

		return ParserResult{nil, input}
	}
}

// Fail simply returns a failed result
var Fail Parser = func(input ParserInput) ParserResult {
	return ParserResult{nil, input}
}

type RuneArrayInput struct {
	Text            []rune
	CurrentPosition int
}

func (input RuneArrayInput) RemainingInput() ParserInput {
	if input.CurrentPosition+1 >= len(input.Text) {
		return nil
	}

	return RuneArrayInput{input.Text, input.CurrentPosition + 1}
}

func (input RuneArrayInput) CurrentCodePoint() rune {
	if input.CurrentPosition >= len(input.Text) {
		return '\x00'
	}

	return input.Text[input.CurrentPosition]
}

func StringToInput(input string) ParserInput {
	return RuneArrayInput{[]rune(input), 0}
}

func ToString(input interface{}) interface{} {
	var builder strings.Builder

	for e := input.(*list.List).Front(); e != nil; e = e.Next() {
		builder.WriteRune(e.Value.(rune))
	}

	return builder.String()
}
