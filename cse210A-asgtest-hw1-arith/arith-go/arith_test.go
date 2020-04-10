package main

import (
	"container/list"
	"testing"
)

func TestNumber(t *testing.T) {
	var parser = Number()

	var res = parser(StringToInput("123"))

	if res.Result == nil || (res.Result != nil && res.Result.(string) != "123") {
		t.Errorf("Failed to parse number")
	}
}

func TestParseInt(t *testing.T) {
	var parser = Number().Map(parseInt)

	var res = parser(StringToInput("-        123"))

	if res.Result == nil || (res.Result != nil && res.Result.(int) != -123) {
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
