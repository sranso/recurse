# recursively sort first half of input array
# recursively sort second half of input array
# merge two sorted sublists into one

def mergesort(array):
    half = len(array)/2
    input1 = array[:half]
    input2 = array[half:]
    merge(mergesort(input1), mergesort(input2))

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
