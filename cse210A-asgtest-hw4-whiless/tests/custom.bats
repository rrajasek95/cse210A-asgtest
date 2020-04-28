load harness

@test "custom-1" {
  check 'if true ∧ -3 < -14 then x := -1 else y := 2' '⇒ y := 2, {}
⇒ skip, {y → 2}'
}

@test "custom-2" {
  check 'if ( 0 - 0 ) < 0 then z8 := 09 else z3 := 90' '⇒ z3 := 90, {}
⇒ skip, {z3 → 90}'
}

@test "custom-3" {
  check 'z := ( x8 - 1 ) * -4' '⇒ skip, {z → 4}'
}

@test "custom-4" {
  check 'x := y - (( -2 ))' '⇒ skip, {x → 2}'
}

@test "custom-5" {
  check 'while false ∧ true ∧ false ∨ false do x := 3' '⇒ skip, {}'
}