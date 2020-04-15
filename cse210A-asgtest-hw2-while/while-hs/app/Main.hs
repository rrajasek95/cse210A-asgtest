module Main where

import While
import Data.Map (empty, fromList)
main :: IO ()
main = do
    a <- getLine
    putStrLn $ showState $ interpret a
