module Main where

import While
import Data.Map (empty, fromList)
main :: IO ()
main = do
    a <- getLine
    print $ flip evalA (Environment (fromList [("test", 22)]) empty) $ run a
