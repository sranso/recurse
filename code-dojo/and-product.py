# problem: https://www.hackerrank.com/challenges/and-product
# alt soln: https://github.com/dputtick/rc_code_dojo/blob/master/august_16.py

import fileinput
from functools import reduce

n = int(input())

for i in range(n):
    line = input()
    first, second = list(map(int, line.split()))
    val = reduce(lambda first, second: first & second, range(first, second + 1))
    print(val)
