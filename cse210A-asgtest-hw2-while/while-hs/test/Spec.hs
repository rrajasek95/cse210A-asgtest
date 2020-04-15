import Test.Hspec
import Test.QuickCheck
import Control.Exception (evaluate)

import While
import Data.Map (empty, fromList)

combinatorSuite :: Spec
combinatorSuite = let 
    parseFail = Right "Parser failed to consume entire stream" 
    undefinedError = Right "Undefined parser error." in do
    describe "While.runParser" $ do
        it "should return result when entire stream appears to have been parsed" $ do
            runParser (Parser $ \s -> [(1, "")]) "" `shouldBe` (1 :: Int)
        -- ToDo come up with alternate error handling mechanism

    describe "While.runParserEither" $ do
        it "should return Left value when entire stream is consumed" $ do
            runParserEither (Parser $ \s -> [(1, "")]) "" `shouldBe` Left (1 :: Int)
        it "should return Right \"Parser failed to consume entire stream\" when entire stream fails to be consumed" $ do
            runParserEither (Parser $ \s -> [(1, "test")]) "test" `shouldBe` parseFail

    describe "While.unit" $ do
        it "should wrap the value 1" $ do
            (runParser (unit 1) "") `shouldBe` (1 :: Int)

    describe "While.item" $ do
        it "should parse a single character from the stream" $ do
            (runParser item "t") `shouldBe` 't'

    describe "While.satisfy" $ do
        it "should fail when parsing an empty string (item parse failure)" $ do
            runParserEither (satisfy (\c -> True )) "" `shouldBe` undefinedError

        it "should parse a single character and succeed if predicate matches" $ do
            (runParser (satisfy ('a' == ))) "a" `shouldBe` 'a'
        it "should fail to parse if predicate fails to match" $ do
            (runParserEither (satisfy ('a' == ) )) "b" `shouldBe` undefinedError

-- Parsing of primitives for higher order parsers
primitiveSuite :: Spec
primitiveSuite = do
    describe "While.natural" $ do
        it "should parse a natural number" $ do
            runParser natural "123" `shouldBe` (123 :: Integer)

    describe "While.string" $ do
        it "should match a string" $ do
            runParser (string "while") "while" `shouldBe` "while"
    
    describe "While.spaces" $ do
        it "should match a sequence of spaces" $ do
            runParser spaces "   " `shouldBe` "   "

    describe "While.number" $ do
        it "should parse positive numbers" $ do
            runParser number "123" `shouldBe` (123 :: Int)
        it "should parse negative numbers" $ do
            runParser number "-123" `shouldBe` (-123 :: Int)
    
    describe "While.token" $ do
        it "should compose with a parser and discard trailing spaces" $ do
            runParser (token number) "-123     " `shouldBe` (-123 :: Int)

    describe "While.boolLit" $ do
        it "should parse true as True" $ do
            runParser boolLit "true" `shouldBe` True
        it "should parse false as False" $ do
            runParser boolLit "false" `shouldBe` False


--- Test eval of arithmetic expressions 
aexprSuite :: Spec
aexprSuite = let
        initState = Environment empty empty
        
        xIs10State = Environment (fromList [("x", 10)]) empty

        lit1 = ALit 1
        lit2 = ALit 2
        lit3 = ALit 3

        addExpr = Add lit1 lit2
        subExpr = Sub lit1 lit2
        mulExpr = Mul lit2 lit3
        subMul = Sub lit1 mulExpr
        powExpr = Pow lit2 lit3
        varExpr = NumVar (Var "x")
    in do
    describe "While.evalA" $ do
        it "should eval 2 to 2" $ do
            evalA lit2 initState `shouldBe` 2
        it "should compute 1 + 2 = 3" $ do
            evalA addExpr initState `shouldBe` 3
        it "should compute 1 - 2 = -1" $ do
            evalA subExpr initState `shouldBe` -1
        it "should compute 2 * 3 = 6" $ do
            evalA mulExpr initState `shouldBe` 6
        it "should compute 2 ^ 3 = 8" $ do
            evalA powExpr initState `shouldBe` 8
        it "should compute 1 - 2 * 3 = 5" $ do
            evalA subMul initState `shouldBe` -5
        it "should evaluate x to 0 when S[]" $ do
            evalA varExpr initState `shouldBe` 0
        it "should evaluate x to 10 when S[x:=10]" $ do
            evalA varExpr xIs10State `shouldBe` 10
        it "should evaluate x + x to 20 when S[x:=10]" $ do
            evalA (Add varExpr varExpr) xIs10State `shouldBe` 20

-- Test eval of boolean expressions
bexprSuite :: Spec
bexprSuite = let
    initState = Environment empty empty
    xIsTrueState = Environment empty (fromList [("x", True)])
    lit1 = BLit True
    lit2 = BLit False

    alit1 = ALit 1
    alit2 = ALit 2
    eqExpr = BEq alit1 alit2
    lteExpr = BLTE alit1 alit2
    negExpr = BNeg lit1
    varExpr = BoolVar (Var "x")
    in do
    describe "While.evalB" $ do
        it "should eval true to true" $ do
            evalB lit1 initState `shouldBe` True
        it "should eval false to false" $ do
            evalB lit2 initState `shouldBe` False

        it "should eval 1 <= 2 to True" $ do
            evalB lteExpr initState `shouldBe` True

        it "should eval 1 = 2 to False" $ do
            evalB eqExpr initState `shouldBe` False

        it "should eval not true to False" $ do
            evalB negExpr initState `shouldBe` False
        it "should eval true and true to True" $ do
            evalB (BAnd lit1 lit1) initState `shouldBe` True
        it "should eval true and false to False" $ do
            evalB (BAnd lit1 lit2) initState `shouldBe` False
        it "should eval (1 <= 2) and (2 <= 1) to False" $ do
            evalB (BAnd lteExpr (BLTE alit2 alit1)) initState `shouldBe` False
        it "should eval x to False when S[]" $ do
            evalB varExpr initState `shouldBe` False
        it "shoule eval ~x to True when S[]" $ do
            evalB (BNeg varExpr) initState `shouldBe` True

        it "should eval x to true when S[x:=true]" $ do
            evalB varExpr xIsTrueState `shouldBe` True
        it "should eval ~x to False when S[x:=true]" $ do
            evalB (BNeg varExpr) xIsTrueState `shouldBe` False

stmtSuite :: Spec
stmtSuite = let
        initState = Environment empty empty
        xIs10State = Environment (fromList [("x", 10)]) empty
        xIsTrueState = Environment empty (fromList [("x", True)])
    in do
    describe "While.evalS" $ do
        it "should evaluate skip with state S[] to yield S[]" $ do
            evalS Skip initState `shouldBe` initState
        it "should evaluate x:= 10 with state S[] to yield[x:=10]" $ do
            evalS (AAssg (Var "x") (ALit 10)) initState `shouldBe` xIs10State
        it "should evaluate x:= true with state S[] to yield[x:=true]" $do
            evalS (BAssg (Var "x") (BLit True)) initState `shouldBe` xIsTrueState


whileSuite :: Spec
whileSuite = let
        initState = Environment empty empty
        xIs10State = Environment (fromList [("x", 10)]) empty
        
    in do
    describe "While.interpret" $ do
        it "should eval the program 'skip' to S[]" $ do
            interpret "skip" `shouldBe` initState
        it "should eval the program 'x:=10' to S[x:=10]" $ do
            interpret "x:=10" `shouldBe` xIs10State
        it "should eval the program 'skip;x:=10' to S[x:=10]" $ do
            interpret "skip;x:=10" `shouldBe` xIs10State
        it "should eval the program 'x :=   10;skip' to S[x:=10]" $ do
            interpret "x :=   10;  skip   " `shouldBe` xIs10State
        it "should eval the program 'if true then x:= 10 else skip' to S[x:=10]" $ do
            interpret "if true then x:= 10 else skip" `shouldBe` xIs10State
        it "should eval the program 'if false then x:= 10 else skip' to S[]" $ do
            interpret "if false then x:= 10 else skip" `shouldBe` initState
        it "should interpret the program 'while x <= 9 do x:= x + 1' to S[x:=10]" $ do
            interpret "while x <= 9 do x:= x + 1" `shouldBe` xIs10State

main :: IO ()
main = hspec $ do
    combinatorSuite
    primitiveSuite
    aexprSuite
    bexprSuite
    stmtSuite
    whileSuite