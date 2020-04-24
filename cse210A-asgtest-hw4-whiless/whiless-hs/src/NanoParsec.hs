module NanoParsec where
    
import Control.Applicative
import Control.Monad

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
    case runParserDebug p a of
        Left l -> l
        Right r -> error r

runParserDebug :: Parser a -> String -> Either a String
runParserDebug p a =
    case parse p a of
        [(res, [])] -> Left res
        [(_, rs)] -> Right ("Parser failed to consume entire stream " ++ rs)
        _ -> Right "Undefined parser error."


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

