package main

import (
	"fmt"
	"strconv"
	"unicode"
)

/* I start defining the specific parsers and predicates for ARITH here */
func isDigit(codePoint interface{}) bool {
	return unicode.IsDigit(codePoint.(rune))
}

func isWhitespace(codePoint interface{}) bool {
	return unicode.IsSpace(codePoint.(rune))
}

// func Multiplicand() Parser {
// 	return func(input ParserInput) ParserResult {
// 		return NumericLiteral()
// 	}
// }

func Whitespace() Parser {
	return OneOrMore(Satisfy(AnyChar(), isWhitespace))
}

func WrapWhitespace(parser Parser) Parser {
	return Whitespace().Optional().AndThen(parser).Right()
}

func toNumericString(res interface{}) interface{} {
	var p = res.(Pair)
	var sign, isString = p.First.(string)
	var num, _ = p.Second.(string)

	if isString {
		return sign + num
	} else {
		return num
	}
}

func NumericLiteral() Parser {
	return Whitespace().Optional().AndThen(OneOrMore(Satisfy(AnyChar(), isDigit))).Right().Map(ToString)
}

func Number() Parser {
	return ExpectString("-").Optional().AndThen(NumericLiteral()).Map(toNumericString)
}

func parseInt(arg interface{}) interface{} {
	var result, _ = strconv.Atoi(arg.(string))
	return result
}

/* Main function which reads a line of input and outputs the resultant arithmetic expression */
func main() {
	fmt.Println("Hello, world.")
}
