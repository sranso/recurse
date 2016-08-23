-- https://projecteuler.net/problem=35

import Data.List (nubBy)

primeList :: Integer -> [Integer]
primeList n = nubBy (\y x-> x`mod`y==0) [2..n]

-- primes = primeList 1000000
primes = primeList 100

rotations :: Integer -> [Integer]
rotations x = map read $ filter (\x -> head x /= '0') $ take l (iterate step (show x))
  where l = length (show x)

step :: String -> String
step (x:xs) = xs ++ [x]

check :: Integer -> Bool
check x =  x `elem` (takeWhile (<= x) primes)


checkAll :: [Integer] -> Bool
checkAll x = and $ map check x

checkRotations :: Integer -> Bool
checkRotations x = checkAll $ rotations x

circular = filter checkRotations primes
