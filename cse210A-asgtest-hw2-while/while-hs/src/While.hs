module While where

import Data.Char
import Data.Map
import Control.Monad
import Control.Applicative

{-
Code adapted from the "Write You A Haskell" tutorial by Stephen Diehl:
http://dev.stephendiehl.com/fun/002_parsers.html#parser-combinators

The code defines parser combinators used for an arithmetic parsing language
-}

-- A parser is a function that accepts a string and converts it to some object
-- for e.g. a keyword parser could take a reserved keyword such as "while" and map it to a While type
newtype Parser a = Parser { parse  :: String -> [(a, String)]}

-- runParser takes a parser and executes it on a string to get our desired object
-- it effectively "unwraps" or parser result
runParser :: Parser a -> String -> a
runParser p a =
    case runParserEither p a of
        Left l -> l
        Right r -> error r

runParserEither :: Parser a -> String -> Either a String
runParserEither p a =
    case parse p a of
        [(res, [])] -> Left res
        [(_, rs)] -> Right "Parser failed to consume entire stream"
        _ -> Right "Undefined parser error."

-- item parses a single character from stream
item :: Parser Char
item = Parser $ (\s ->
    case s of
        [] -> []
        (c:cs) -> [(c, cs)])

-- bind accepts a parser and a parser generating function to produce a "composed" parser
-- the original parser produces [(a, String)]
-- So we call the function parse over (f a) and the remaining string s' to yield
-- [[(b, String)]]. We flatMap this using concatMap
bind :: Parser a -> (a -> Parser b) -> Parser b
bind p f = Parser $ \s -> concatMap (\(a, s') -> parse (f a) s') $ parse p s

-- unit injects a value without reading the stream
unit :: a -> Parser a
unit a = Parser $ \s -> [(a, s)]

-- Reminder, a functor is a category (F a) to (F b). map must implement  F a -> (a -> b) -> F b
instance Functor Parser where
    fmap f (Parser cs)  = Parser $ \s -> [ (f a, s') | (a, s') <- cs s]

-- An applicative must implement <*> that takes F (a -> b) -> F a -> F b
-- this one is a lot more confusing in comparison to others. 
-- Basic idea is that it takes an embedded context function and 
-- applies it to an embedded context argument
instance Applicative Parser where
    pure = return
    
    -- this one deserves a bit more explanation
    -- since the sequence is important
    -- we perform (f, s1) <- cs1 s as a first step of parsing that yields a function we can apply
    -- we then perform (a, s2) <- cs2 s1 as a second parsing step
    -- Now, we know s2 is the remnant string to parse, 
    -- so it must be of the form (f a, s2)
    (Parser cs1) <*> (Parser cs2) = Parser $ \s -> [(f a, s2) | (f, s1) <- cs1 s, (a, s2) <- cs2 s1]

instance Monad Parser where
    return = unit
    (>>=) = bind

-- The parser has a failure state where it stops reading the stream
instance MonadPlus Parser where
    mzero = failure
    mplus = combine

instance Alternative Parser where
    empty = mzero
    (<|>) = option

-- This is a parser that does a "parallel parse"
combine :: Parser a -> Parser a -> Parser a
combine p q = Parser (\s -> parse p s ++ parse q s)

-- This is easy, create a parser that returns an empty array
-- This defines the notion of a `zero` and a "kind of" addition
-- empty <|> p = p = p <|> empty
failure :: Parser a
failure =  Parser $ (\cs -> [])

-- This is the easiest to understand, if parse p fails, then try parsing q
option :: Parser a -> Parser a -> Parser a
option p q = Parser $ \s ->
    case parse p s of
        [] -> parse q s
        res -> res

-- Satisfy creates a parser that succeeds if a predicate is satisfied
-- else fails
satisfy :: (Char -> Bool) -> Parser Char
satisfy p = item `bind` \c ->
    if p c then unit c
    else (Parser (\cs -> []))

-- oneOf checks if the character is one of a list
oneOf :: [Char] -> Parser Char
oneOf s = satisfy (\c -> c `elem` s)

-- Creates a parser that executes a binary computation or returns a default
chainl :: Parser a -> Parser (a -> a -> a) -> a -> Parser a
chainl p op a = (p `chainl1` op) <|> return a

-- Chainl1 can be visualized in the grammar as
chainl1 :: Parser a -> Parser (a -> a -> a) -> Parser a
p `chainl1` op = do {
    a <- p; rest a}
    where rest a = (do f <- op;
                       b <- p;
                       rest (f a b)) <|> return a


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
variable = Var <$> some (satisfy isAlpha)

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
    deriving (Show)

data BExpr
    = BLit Bool
    | BEq AExpr AExpr
    | BLTE AExpr AExpr
    | BNeg BExpr
    | BAnd BExpr BExpr
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
infixOp x f = reserved x >> return f

addop :: Parser (AExpr -> AExpr -> AExpr)
addop = (infixOp "+" Add) <|> (infixOp "-" Sub)

mulop :: Parser (AExpr -> AExpr -> AExpr)
mulop = infixOp "*" Mul

powop :: Parser (AExpr -> AExpr -> AExpr)
powop = infixOp "^" Pow

-- Boolean AST parsers
bool :: Parser BExpr
bool = do
    b <- boolLit
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
    v <- variable
    reserved ":="
    a <- aExpr

    return (AAssg v a)


assignment :: Parser Stmt
assignment = arithAssignment


stmt :: Parser Stmt
stmt = (skip <|> assignment) `chainl1` seqOp

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
    BNeg b -> not (evalB b env)
    BAnd b1 b2 -> (evalB b1 env) && (evalB b2 env)


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

run :: String -> AExpr
run = runParser aExpr