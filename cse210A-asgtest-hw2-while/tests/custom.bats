load harness

@test "custom-1" {
  check 'x := (true ? 1 : 2 )' '{x → 1}'
}

@test "custom-2" {
  check 'x := (false ? 1 : 2)' '{x → 2}'
}

@test "custom-3" {
  check 'y := 3 ; x := (false ? 1 : 2 ) + y' '{x → 5, y → 3}'
}

@test "custom-4" {
  check 'x:= (true ? 1 : 2) + (false ? 1 : 2)' '{x → 3}'
}

@test "custom-5" {
  check 'x:= (false ? 1 : (true ? 2 : 3))' '{x → 2}'
}