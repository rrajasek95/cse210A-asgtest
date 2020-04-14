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
main :: IO ()
main = hspec $ do
    combinatorSuite