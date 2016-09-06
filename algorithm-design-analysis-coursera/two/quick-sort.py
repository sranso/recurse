import math
import pdb
import unittest
from hypothesis import given
import hypothesis.strategies as st

array = []

#with open('./QuickSort.txt') as f:
#    for line in f:
#        array.append(int(line))

def brute_force(array):
    for o in range(0, len(array) - 1):
        for i in range(o + 1, len(array)):
            if array[o] > array[i]:
                temp = array[o]
                array[o] = array[i]
                array[i] = temp
    return array

# QuickSort(array A, length n)
# if n = 1 return
# p = ChoosePivot(A, n)
# partition A around p
# recursively sort 1st part
# recursively sort 2nd part

def quick_sort(array, n):
    if n <= 1:
        return array
    p = partition(array, 0, n - 1)
    l = array[:p]
    r = array[p:]
    print('left:', l)
    print('right:', r)
    quick_sort(l, len(l))
    quick_sort(r, len(r))
    return array

# Partition(A, l, r), input ~= A[l..r]
# p = A[l]
# i = l + 1
# for j = l + 1 to r
#   if A[j] < p [if A[j] > p, do nothing]
#     swap A[j] and A[i]
#     i += i
# swap A[l] and A[i-1]

def partition(array, l, r):
    p = array[l]
    i = l + 1 # i -> the latest pivot
    for j in range(l + 1, r): # j -> where we are in list
        if array[j] < p:
            swap(array, j, i)
            i += 1
    swap(array, l, i - 1)
    pdb.set_trace()
    return i

def swap(array, l, r):
    temp = array[l]
    array[l] = array[r]
    array[r] = temp
    return array

#class TestQuickSort(unittest):
#    @given(st.lists(st.integers()))
#    def test_quick_sort_vs_brute_force(self, array):
#        copy = array[:]
#        self.assertEqual(brute_force(array), quick_sort(array))
#
#if __name__ == '__main__':
#    unittest.main()

ar = [3,2,1,6,4,5]
print(quick_sort(ar, len(ar)))
