load harness

@test "custom-1" {
    check '3                      - 1' '2'
}

@test "custom-2" {
    check '3                      - (1 - 2)' '4'
}

@test "custom-3" {
    check ' 1*2*3*4*5*6*7*8*9*(10)       ' '3628800'
}

@test "custom-4" {
    check '222222 + 4 - 7 * 3' '222205'
}

@test "custom-5" {
    check '-1' '-1' 
}