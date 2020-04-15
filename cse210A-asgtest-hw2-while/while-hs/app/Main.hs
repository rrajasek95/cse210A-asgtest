module Main where

import While

main :: IO ()
main = do
    a <- getLine
    print $ evalA $ run a
