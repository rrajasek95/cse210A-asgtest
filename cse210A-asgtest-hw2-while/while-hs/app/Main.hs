module Main where

import While
import Data.Map (empty, fromList)
main :: IO ()
main = do
    a <- getLine
    print $ flip evalA empty $ run a
