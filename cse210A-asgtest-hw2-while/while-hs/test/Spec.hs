import Test.Hspec
import Test.QuickCheck
import Control.Exception (evaluate)

import While

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
        lit1 = ALit 1
        lit2 = ALit 2
        lit3 = ALit 3

        addExpr = Add lit1 lit2
        subExpr = Sub lit1 lit2
        mulExpr = Mul lit2 lit3
        subMul = Sub lit1 mulExpr
        powExpr = Pow lit2 lit3
    in do
    describe "While.evalA" $ do
        it "should eval 2 to 2" $ do
            evalA lit2 `shouldBe` 2
        it "should compute 1 + 2 = 3" $ do
            evalA addExpr `shouldBe` 3
        it "should compute 1 - 2 = -1" $ do
            evalA subExpr `shouldBe` -1
        it "should compute 2 * 3 = 6" $ do
            evalA mulExpr `shouldBe` 6
        it "should compute 2 ^ 3 = 8" $ do
            evalA powExpr `shouldBe` 8
        it "should compute 1 - 2 * 3 = 5" $ do
            evalA subMul `shouldBe` -5

-- Test eval of boolean expressions
bexprSuite :: Spec
bexprSuite = let
    lit1 = BLit True
    lit2 = BLit False

    alit1 = ALit 1
    alit2 = ALit 2
    eqExpr = BEq alit1 alit2
    lteExpr = BLTE alit1 alit2
    negExpr = BNeg lit1
    in do
    describe "While.evalB" $ do
        it "should eval true to true" $ do
            evalB lit1 `shouldBe` True
        it "should eval false to false" $ do
            evalB lit2 `shouldBe` False

        it "should eval 1 <= 2 to True" $ do
            evalB lteExpr `shouldBe` True

        it "should eval 1 = 2 to False" $ do
            evalB eqExpr `shouldBe` False

        it "should eval not true to False" $ do
            evalB negExpr `shouldBe` False
        it "should eval true and true to True" $ do
            evalB (BAnd lit1 lit1) `shouldBe` True
        it "should eval true and false to False" $ do
            evalB (BAnd lit1 lit2) `shouldBe` False
        it "should eval (1 <= 2) and (2 <= 1) to False" $ do
            evalB (BAnd lteExpr (BLTE alit2 alit1)) `shouldBe` False

main :: IO ()
main = hspec $ do
    combinatorSuite
    primitiveSuite
    aexprSuite
    bexprSuite