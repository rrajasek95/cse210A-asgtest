package main

import (
	"container/list"
	"testing"
)

func TestExpectCodePoint(t *testing.T) {

	var parser = ExpectCodePoint('a')
	var res = parser(StringToInput("a"))

	if res.Result == nil {
		t.Errorf("Expected to parse rune 'a' but failed")
	}

	var res2 = parser(StringToInput("b"))

	if res2.Result != nil {
		t.Errorf("Expected to fail parse rune 'b' but succeeded")
	}
}

func TestExpectCodePoints(t *testing.T) {
	var expectedRune = []rune("test")
	var parser = ExpectCodePoints(expectedRune)
	var res = parser(StringToInput("test"))

	if res.Result == nil {
		t.Errorf("Expected to parse rune array 'test' but failed")
	}

	var res2 = parser(StringToInput("testtt"))

	if res2.Result == nil {
		t.Errorf("Expected to parse rune array 'test' but failed")
	}

	var res3 = parser(StringToInput("tes"))

	if res3.Result != nil {
		t.Errorf("Expected to fail parse, but succeeded")
	}
}

func TestOrElse(t *testing.T) {
	var expectedRune1 = []rune("test")
	var expectedRune2 = []rune("hello")

	var parser = ExpectCodePoints(expectedRune1).OrElse(ExpectCodePoints(expectedRune2))

	var res1 = parser(StringToInput("test"))
	var res2 = parser(StringToInput("hello"))

	if res1.Result == nil || res2.Result == nil {
		t.Errorf("Expected alternative parses to succeed but failed")
	}

	var res3 = parser(StringToInput("howdy"))

	if res3.Result != nil {
		t.Errorf("Expected alternative parse to fail but succeeded")
	}
}

func TestRepeated(t *testing.T) {
	var expectedRune = []rune("test")

	var parser = Repeated(ExpectCodePoints(expectedRune))

	var res1 = parser(StringToInput("testtesttestt"))

	if res1.Result == nil && res1.Result.(*list.List).Len() == 3 {
		t.Errorf("Expected to parse three instances of test but failed")
	}
}

func TestAnyChar(t *testing.T) {
	var parser = AnyChar()

	var res1 = parser(StringToInput(""))
	var res2 = parser(StringToInput("abc"))

	if res1.Result != nil {
		t.Errorf("Expected to fail to parse due to empty input")
	}

	if res2.Result == nil {
		t.Errorf("Expected to parse single character successfully")
	}
}

func TestOneOrMore(t *testing.T) {
	var parser = OneOrMore(AnyChar())

	var res1 = parser(StringToInput("123"))

	if res1.Result == nil {
		t.Errorf("Expected to parse the input successfully")
	}

	var res2 = parser(StringToInput("1234abc"))

	if res2.Result == nil {
		t.Errorf("Expected to parse input successfully")
	}
}
