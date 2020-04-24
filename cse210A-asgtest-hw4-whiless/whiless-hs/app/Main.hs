module Main where

import While
import Data.Map (empty, fromList)
main :: IO ()
main = do
    a <- getLine
    putStrLn $ showSteps $ init $ interpretSS a
