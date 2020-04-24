import Test.Hspec
import Test.QuickCheck
import Control.Exception (evaluate)

import NanoParsec
import While
import Data.Map (empty, fromList)

smallStepSuite :: Spec
smallStepSuite  = let
        initState = Environment empty empty
        xIs10State = Environment (fromList [("x", 10)]) empty
        xIsTrueState = Environment empty (fromList [("x", True)])

        assgX10 = AAssg (Var "x") (ALit 10)
        assgY20 = AAssg (Var "y") (ALit 20)
        assgZ30 = AAssg (Var "z") (ALit 30)
    in do
    describe "While.evalS" $ do
        it "should evaluate skip with state S[] to yield S[]" $ do
            smallStepEvalS Skip initState `shouldBe` (Skip, initState)
        it "should evaluate x:= 10 with state S[] to yield[x:=10]" $ do
            smallStepEvalS (AAssg (Var "x") (ALit 10)) initState `shouldBe` (Skip, xIs10State)
        it "should evaluate 'skip; x:=10' with state S[] to yield ('x:=10', S[])" $ do
            smallStepEvalS (Seq Skip (AAssg (Var "x") (ALit 10))) initState `shouldBe` ((AAssg (Var "x") (ALit 10)), initState)
        it "should evaluate 'x:=10; y:= 20' with state S[] to yield ('skip; y:= 20', S[ x := 10])" $ do
            smallStepEvalS (Seq assgX10 assgY20) initState `shouldBe` (Seq Skip assgY20, xIs10State)
        it "should evaluate '{x := 10 ; y := 20} ; z := 30' to yield ('skip; y := 20 ; z := 30', S[ x := 10])" $ do
            smallStepEvalS (Seq (Seq assgX10 assgY20) assgZ30) initState `shouldBe` (Seq (Seq Skip assgY20) assgZ30, xIs10State)
        it "should evaluate 'skip; y := 20 ; z := 30' with S[x:= 10] to yield ('y:=20 ; z := 30', S[x:=10])" $ do
            smallStepEvalS (Seq (Seq Skip assgY20) assgZ30) xIs10State `shouldBe` ((Seq assgY20 assgZ30), xIs10State)
main :: IO ()
main = hspec $ do
    smallStepSuite