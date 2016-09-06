import math
import unittest
from hypothesis import given
import hypothesis.strategies as st

# recursively sort first half of input array
# recursively sort second half of input array
# merge two sorted sublists into one

def brute_force(array):
    for o in range(0, len(array) - 1):
        for i in range(o + 1, len(array)):
            if array[o] > array[i]:
                temp = array[o]
                array[o] = array[i]
                array[i] = temp
    return array

def merge_sort(array):
    half = int(math.floor(len(array) / 2))
    input1 = array[:half]
    input2 = array[half:]
    # TODO fix max recursion depth error
    merge(merge_sort(input1), merge_sort(input2))

def merge(input1, input2):
    merged = []
    i = 0
    j = 0
    while i < len(input1) and j < len(input2):
        if input1[i] < input2[j]:
            merged.append(input1[i])
            i = i + 1
        else:
            merged.append(input2[j])
            j = j + 1

    while i < len(input1):
        merged.append(input1[i])
        i = i + 1

    while j < len(input2):
        merged.append(input2[j])
        j = j + 1

    return merged

class TestCountInversions(unittest.TestCase):
    @given(st.lists(st.integers()))
    def test_merge_sort_vs_brute_force(self, array):
        copy = array[:] # in case one of our methods mutates its input array.
        self.assertEqual(brute_force(array), merge_sort(copy))

if __name__ == 'main':
    unittest.main()

