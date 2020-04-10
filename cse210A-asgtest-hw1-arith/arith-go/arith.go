package main

import (
	"bufio"
	"os"
	"strconv"
	"unicode"
)

// Expr interface that all types must implement
type Expr interface {
	Eval() int
}

type IntExpr struct {
	Val int
}

func (expr IntExpr) Eval() int {
	return expr.Val
}

type SumExpr struct {
	left  Expr
	right Expr
}

func (expr SumExpr) Eval() int {
	return expr.left.Eval() + expr.right.Eval()
}

type MulExpr struct {
	left  Expr
	right Expr
}

func (expr MulExpr) Eval() int {
	return expr.left.Eval() * expr.right.Eval()
}

type SubExpr struct {
	left  Expr
	right Expr
}

func (expr SubExpr) Eval() int {
	return expr.left.Eval() - expr.right.Eval()
}

type PowExpr struct {
	left  Expr
	right Expr
}

func (expr PowExpr) Eval() int {
	return pow(expr.left.Eval(), expr.right.Eval())
}

/* I start defining the specific parsers and predicates for ARITH here */
func isDigit(codePoint interface{}) bool {
	return unicode.IsDigit(codePoint.(rune))
}

func isDigitRune(codePoint rune) bool {
	return rune('0') <= codePoint && codePoint <= rune('9')
}

var ExpectNumber Parser = expect("-").Optional().AndThen(MaybeSpacesBefore(ExpectSeveral(isDigitRune, isDigitRune)))

func isSpaceChar(codePoint rune) bool {
	return codePoint == rune(' ') || codePoint == rune('\n') ||
		codePoint == rune('\r') || codePoint == rune('\t')
}

var ExpectSpaces Parser = ExpectSeveral(isSpaceChar, isSpaceChar).Optional()

func isWhitespace(codePoint interface{}) bool {
	return unicode.IsSpace(codePoint.(rune))
}

func MaybeSpacesBefore(parser Parser) Parser {
	return Parser(ExpectSpaces).AndThen(parser).Right()
}

func expect(text string) Parser {
	return MaybeSpacesBefore(ExpectString(text))
}

func Multiplicand(input ParserInput) ParserResult {
	return Parser(Exponand).AndThen(expect("^")).Left().AndThen(Exponand).Map(func(res interface{}) interface{} {
		var p = res.(Pair)

		var e1 = p.First.(Expr)
		var e2 = p.Second.(Expr)

		return PowExpr{e1, e2}
	}).OrElse(Exponand)(input)
}

func Addend(input ParserInput) ParserResult {
	return Parser(Multiplicand).Bind(func(firstResult interface{}) Parser {
		return expect("*").AndThen(Multiplicand).RepeatAndFoldLeft(firstResult, multiply)
	})(input)
}

func Exponand(input ParserInput) ParserResult {
	return ExpectNumber.Map(toNumericString).Map(readInt).OrElse(
		expect("(").AndThen(
			Expression).AndThen(expect(")")).Left().Right())(input)
}

func Expression(input ParserInput) ParserResult {
	return Parser(Addend).Bind(func(firstResult interface{}) Parser {
		return expect("+").OrElse(expect("-")).AndThen(Addend).RepeatAndFoldLeft(firstResult, add)
	})(input)
}

func Whitespace() Parser {
	return OneOrMore(Satisfy(AnyChar(), isWhitespace))
}

func WrapWhitespace(parser Parser) Parser {
	return Whitespace().Optional().AndThen(parser).AndThen(Whitespace().Optional()).Left().Right()
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
	return ExpectNumber.Map(ToString)
}

func multiply(lhs interface{}, rhs interface{}) interface{} {
	return MulExpr{lhs.(Expr), GetSecond(rhs).(Expr)}
}

func add(lhs interface{}, rhs interface{}) interface{} {
	if "+" == GetFirst(rhs).(string) {
		return SumExpr{lhs.(Expr), GetSecond(rhs).(Expr)}
	} else {
		return SubExpr{lhs.(Expr), GetSecond(rhs).(Expr)}
	}
}

func exp(lhs interface{}, rhs interface{}) interface{} {
	return PowExpr{lhs.(Expr), GetSecond(rhs).(Expr)}
}

/* Naive integer exponentiation */
func pow(a, b int) int {
	var i, result int
	result = 1
	for i = 0; i < b; i++ {
		result *= a
	}
	return result
}

func readInt(arg interface{}) interface{} {
	var result, _ = strconv.Atoi(arg.(string))
	return IntExpr{result}
}

func parseInt(arg interface{}) interface{} {
	var result, _ = strconv.Atoi(arg.(string))
	return result
}

/* Main function which reads a line of input and outputs the resultant arithmetic expression */
func main() {
	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	println(Expression(StringToInput(text)).Result.(Expr).Eval())
}
