# Test scripts for CSE201A

Please merge your homework with the repepctive test script repository. You should include a *Makefile* 
such that running make in the root directory of your submission produces a file in the root directory.
The file, when executed, should read the strings via stdin and output the required content via stdout.

These test scripts are prepared based on [Sohum Banerjea's work](https://github.com/SohumB/cse210A-asgtest/tree/master).

## Instructions

### Assignment 1

**Assignment 1: ARITH** was implemented in Golang. No additional dependencies are required since all parsing is done using handwritten parser combinators.

The go installation instructions can be followed from https://golang.org/doc/install

To build the executable, simply run
```
make
```

The implementation of ARITH was largely inspired by Armin Heller's posts:
* https://medium.com/@armin.heller/parser-combinator-gotchas-2792deac4531
* https://medium.com/@armin.heller/parser-combinator-gotchas-2792deac4531

The key differences are that the original blog post evaluates the expressions inline instead of building a parse tree and in the assignment, some additional combinators are implemented.
