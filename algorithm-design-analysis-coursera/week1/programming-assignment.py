import math
import unittest
from hypothesis import given
import hypothesis.strategies as st

array = [] # 2407905288

with open('./IntegerArray.txt') as f:
    for line in f:
        array.append(int(line))

def brute_force(array):
    inversions = 0
    for o in range(0, len(array) - 1):
        for i in range(o + 1, len(array)):
            if array[o] > array[i]:
                inversions += 1
    return inversions

def sort_and_count(array):
    if len(array) <= 1:
        return (array, 0)
    else:
        half = int(math.floor(len(array) / 2))
        b, x = sort_and_count(array[:half])
        c, y = sort_and_count(array[half:])
        d, z = merge_and_count_split_inversion(b, c)
        return (d, x + y + z)

def merge_and_count_split_inversion(b, c):
    inversions = 0
    d = []
    i = 0
    j = 0
    while i < len(b) and j < len(c):
        if b[i] <= c[j]:
            d.append(b[i])
            i = i + 1
        else:
            d.append(c[j])
            inversions = inversions + (len(b) - i)
            j = j + 1
    while i < len(b):
        d.append(b[i])
        i = i + 1
    while j < len(c):
        d.append(c[j])
        j = j + 1
    return (d, inversions)


#print(sort_and_count(array)[1])

# to run: python3 -m unittest <file>
class TestCountInversions(unittest.TestCase):
    def test_sort_and_count_vs_brute_force(self):
        three = [2, 4, 1, 3, 5]
        five = [1, 20, 6, 4, 5]
        copy_three = three[:]
        copy_five = five[:]
        self.assertEqual(brute_force(three), sort_and_count(copy_three)[1])
        self.assertEqual(brute_force(five), sort_and_count(copy_five)[1])

    @given(st.lists(st.integers()))
    def test_sort_and_count_vs_brute_force(self, array):
        copy = array[:] # in case one of our methods mutates its input array.
        self.assertEqual(brute_force(array), sort_and_count(copy)[1])

if __name__ == 'main':
    unittest.main()

