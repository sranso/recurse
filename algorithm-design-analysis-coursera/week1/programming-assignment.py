import math
import pdb
array = []

with open('./IntegerArray.txt') as f:
    for line in f:
        array.append(int(line))

def sort_and_count(array):
    if len(array) == 1:
        return [array, 0]
    else:
        half = int(math.floor(len(array) / 2))
        b, x = sort_and_count(array[:half])
        c, y = sort_and_count(array[half:])
        d, z = merge_and_count_split_inversion(b, c)
        return [d, (x + y + z)]

def merge_and_count_split_inversion(b, c):
    inversions = 0
    d = []
    i = 0
    j = 0
    while i < len(b) and j < len(c):
        if b[i] < c[j]:
            d.append(b[i])
            i = i + 1
        else:
            d.append(c[j])
            j = j + 1
            inversions = inversions + 1
    while i < len(b):
        d.append(b[i])
        i = i + 1
    while j < len(c):
        d.append(c[j])
        j = j + 1
    return [d, inversions]

#print(sort_and_count([4,5,6,1,2,3]))
print(sort_and_count(array)[1])
