package main

import (
	"container/list"
	"testing"
)

func TestNumber(t *testing.T) {
	var parser = ExpectNumber.Map(toNumericString)

	var res = parser(StringToInput("123"))

	if res.Result == nil || (res.Result != nil && res.Result.(string) != "123") {
		t.Errorf("Failed to parse number")
	}
}

func TestParseInt(t *testing.T) {
	var parser = ExpectNumber.Map(toNumericString)

	var res = parser(StringToInput("-        123         "))

	if res.Result == nil || (res.Result != nil && res.Result.(string) != "-123") {
		t.Errorf("Failed to parse number")
	}
}

func TestWhitespace(t *testing.T) {
	var parser = Whitespace()
	var res = parser(StringToInput("   "))

	if res.Result == nil || res.Result.(*list.List).Len() != 3 {
		t.Errorf("Failed to parse whitespace")
	}
}

func TestExprEval(t *testing.T) {
	var expr = SumExpr{
		SubExpr{IntExpr{1}, IntExpr{2}},
		MulExpr{IntExpr{3}, IntExpr{4}},
	}

	if expr.Eval() != 11 {
		t.Errorf("Eval failed to evaluate")
	}
}

func TestMultiplicand(t *testing.T) {
	var multip = Multiplicand(StringToInput("123"))

	if multip.Result == nil {
		t.Errorf("Failed to read multiplicand")
	}
}

func TestExpr(t *testing.T) {

	var expr_0 = Expression(StringToInput("1+2"))

	if expr_0.Result == nil || expr_0.Result.(Expr).Eval() != 3 {
		t.Errorf("failed to parse")
	}

	var expr = Expression(StringToInput("1+2+3"))

	if expr.Result == nil || expr.Result.(Expr).Eval() != 6 {
		t.Errorf("Failed to parse expression")
	}

	var expr2 = Expression(StringToInput("1 - 2 * 3    "))

	if expr2.Result == nil || expr2.Result.(Expr).Eval() != -5 {
		t.Errorf("Failed to parse expression")
	}
}
