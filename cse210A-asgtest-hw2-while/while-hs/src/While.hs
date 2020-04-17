module While where

import Control.Applicative
import NanoParsec
import Data.Char
import Data.List (intercalate)
import Data.Map

char :: Char -> Parser Char
char c = satisfy (c ==)

natural :: Parser Integer
natural =  read <$> some (satisfy isDigit)

-- boolLit parses a boolean value
boolLit :: Parser Bool
boolLit = 
    (\s -> case s of
        "true" -> True
        "false" -> False) <$> (string "true" <|> string "false")

-- consider single letter variables for now
variable :: Parser Var
variable = Var <$> (do
    spaces;
    c <- satisfy isAlpha
    s <- many (satisfy (\x -> isAlpha x || isDigit x))

    spaces;
    return ([c] ++ s))

numVariable :: Parser AExpr
numVariable = NumVar <$>(do 
    spaces;    
    v <- variable;
    spaces;
    return v)

-- Parses a string from the stream
-- Isn't this the applicative pattern? We can tweak this later on
string :: String -> Parser String
string [] = return []
string (c:cs) =  do { char c ; string cs ; return (c:cs) }

-- Parse out spaces
token :: Parser a -> Parser a
token p = do {
    a <- p;
    spaces;
    return a;
}

-- Match multiple spaces
spaces :: Parser String
spaces = many $ oneOf " \n\r"

-- mark a string as a space separated token
reserved :: String -> Parser String
reserved s = token (string s)

parens :: Parser a -> Parser a
parens p = do
    reserved "("
    a <- p
    reserved ")"
    return a

-- isDigit is taken from Control.Char
digit :: Parser Char
digit = satisfy isDigit

number :: Parser Int
number = do
        s <- reserved "-" <|> return [] -- Read negative sign or nothing
        cs <- some digit -- Read numbers
        return $ read (s ++ cs) -- Interpret the complete number as an Int

-- Define AST and parsers for the different constructs

data Env a b
    = Environment (Map String a) (Map String b)
    deriving (Eq, Show)

data Var 
    = Var String
    deriving (Show)


data AExpr
    = Add AExpr AExpr
    | Sub AExpr AExpr
    | Mul AExpr AExpr
    | Pow AExpr AExpr
    | ALit Int
    | NumVar Var
    | Tern BExpr AExpr AExpr
    deriving (Show)

data BExpr
    = BLit Bool
    | BEq AExpr AExpr
    | BLTE AExpr AExpr
    | BLT AExpr AExpr
    | BNeg BExpr
    | BAnd BExpr BExpr
    | BOr BExpr BExpr
    | BoolVar Var
    deriving (Show)

data Stmt
    = Skip
    | Seq Stmt Stmt
    | IfStmt BExpr Stmt Stmt
    | WhileStmt BExpr Stmt
    | AAssg Var AExpr
    | BAssg Var BExpr
    deriving (Show)

int :: Parser AExpr
int = do
    spaces
    n <- number
    spaces
    return (ALit n)

-- Arithmetic AST parsers
aExpr :: Parser AExpr
aExpr = aTerm `chainl1` addop

aTerm :: Parser AExpr
aTerm = aFactor `chainl1` mulop

-- TODO: find a more idiomatic construct for this
-- it looks very awkward
aFactor :: Parser AExpr
aFactor = do 
    a <- aPow 
    (do 
        f <- powop
        b <- aFactor
        return (f a b) ) <|> return a

aPow :: Parser AExpr
aPow = int <|> numVariable <|> parens aExpr

-- Matches an operator token and wraps data constructor
infixOp :: String -> (a -> a -> a) -> Parser (a -> a -> a)
infixOp x f = do 
    spaces
    reserved x
    spaces
    return f

addop :: Parser (AExpr -> AExpr -> AExpr)
addop = (infixOp "+" Add) <|> (infixOp "-" Sub)

mulop :: Parser (AExpr -> AExpr -> AExpr)
mulop = infixOp "*" Mul

powop :: Parser (AExpr -> AExpr -> AExpr)
powop = infixOp "^" Pow

-- Boolean AST parsers
equalTo :: Parser BExpr
equalTo = do
    spaces
    a1 <- aExpr
    spaces
    reserved "="
    spaces
    a2 <- aExpr
    spaces
    return (BEq a1 a2)

lessThanEq :: Parser BExpr
lessThanEq = do
    spaces
    a1 <- aExpr
    spaces
    reserved "<="
    spaces
    a2 <- aExpr
    spaces
    return (BLTE a1 a2)

lessThan :: Parser BExpr
lessThan = do
    spaces
    a1 <- aExpr
    spaces
    reserved "<"
    spaces
    a2 <- aExpr
    spaces
    return (BLT a1 a2)

negation :: Parser BExpr
negation = do
    spaces
    reserved "¬"
    spaces
    b <- bExpr
    spaces
    return (BNeg b)

boolPrimitives :: Parser BExpr
boolPrimitives = lessThanEq <|> lessThan <|> equalTo <|> negation <|> bool <|> parens bExpr

bDisjunctive :: Parser BExpr
bDisjunctive = boolPrimitives `chainl1` andOp

bExpr :: Parser BExpr
bExpr = bDisjunctive `chainl1` orOp

andOp :: Parser (BExpr -> BExpr -> BExpr)
andOp = infixOp "∧" BAnd

orOp :: Parser (BExpr -> BExpr -> BExpr)
orOp = infixOp "∨" BOr

bool :: Parser BExpr
bool = do
    spaces
    b <- boolLit
    spaces
    return (BLit b)

-- Stmt AST parsers

skip :: Parser Stmt
skip = 
    do
        reserved "skip"
        return Skip

-- Sequencing is effectively an infix operation (s1 ";" s2)
seqOp :: Parser (Stmt -> Stmt -> Stmt)
seqOp = infixOp ";" Seq

arithAssignment :: Parser Stmt
arithAssignment = do
    spaces
    v <- variable
    spaces
    reserved ":="
    spaces
    a <- aExpr
    spaces
    return (AAssg v a)


assignment :: Parser Stmt
assignment = arithAssignment

ifElse :: Parser Stmt
ifElse = do
    spaces
    reserved "if"
    spaces
    b <- bExpr
    spaces
    reserved "then"
    spaces
    s1 <- stmt
    spaces
    reserved "else"
    spaces
    s2 <- stmt
    spaces
    return (IfStmt b s1 s2)

while :: Parser Stmt
while = do
    spaces
    reserved "while"
    spaces
    b <- bExpr
    spaces
    reserved "do"
    s <- (do reserved "{" ; spaces ; s' <- stmt ; reserved "}"; spaces; return s') <|> simpleStmt

    return (WhileStmt b s)

simpleStmt :: Parser Stmt
simpleStmt = (skip <|> assignment <|> ifElse <|> while)
stmt :: Parser Stmt
stmt =  simpleStmt `chainl1` seqOp

evalA :: AExpr -> Env Int Bool -> Int
evalA ex env@(Environment valMap _) = case ex of
    Add a1 a2 -> evalA a1 env + evalA a2 env
    Sub a1 a2 -> evalA a1 env - evalA a2 env
    Mul a1 a2 -> evalA a1 env * evalA a2 env
    Pow a1 a2 -> (evalA a1 env) ^ (evalA a2 env)
    ALit n     -> n
    NumVar (Var x) -> findWithDefault 0 x valMap


evalB :: BExpr -> Env Int Bool -> Bool
evalB ex env@(Environment _ valMap) = case ex of
    BLit b -> b
    BoolVar (Var x) -> findWithDefault False x valMap
    BEq a1 a2 -> (evalA a1 env) == (evalA a2 env)
    BLTE a1 a2 -> (evalA a1 env) <= (evalA a2 env)
    BLT a1 a2 -> (evalA a1 env) < (evalA a2 env)
    BNeg b -> not (evalB b env)
    BAnd b1 b2 -> (evalB b1 env) && (evalB b2 env)
    BOr b1 b2 -> (evalB b1 env) || (evalB b2 env)


evalS :: Stmt -> Env Int Bool -> Env Int Bool
evalS s env@(Environment aVars bVars) = case s of
    Skip -> env
    Seq s1 s2 -> evalS s2 (evalS s1 env)
    IfStmt b s1 s2 -> if evalB b env then evalS s1 env else evalS s2 env
    WhileStmt b s -> if evalB b env then evalS (WhileStmt b s) (evalS s env) else env
    AAssg (Var x) a -> let arithResult = evalA a env 
        in Environment (insert x arithResult aVars) bVars
    BAssg (Var x) b -> let boolResult = evalB b env
        in Environment aVars (insert x boolResult bVars)


runWhile :: String -> Stmt
runWhile = runParser stmt

interpret :: String -> Env Int Bool
interpret s = flip evalS (Environment Data.Map.empty Data.Map.empty) $ runWhile s

-- Data.Map enforces ordering, so we can rely on that to display our variables in order
showState :: Env Int Bool -> String
showState (Environment aVars _) = 
    let
        arrowMap = [ k ++ " → " ++ show v | (k, v) <- toList aVars]
    in "{" ++ (intercalate ", " arrowMap) ++ "}"
run :: String -> AExpr
run = runParser aExpr