import collections
# http://collabedit.com/4j888

### Sorting problems 
# MERGE AND QUICK SORT

# Divide and Conquer
#  e.g. Add all numbers is array:
#  [1, 2, 3, 4, 5, 6, 7, 8]
#  = [1, 2, 3] + [4, 5, 6] + [7, 8]
#  = 6 + 15 + 15 // processed subproblems
#  = 36 // combine result
#
# Sorting:
# [12, 5, 7, 1, 3, 2, 100]]
#  = [12, 5, 7, 1] + [3, 2, 100]
#  = [12, 5] + [ 7, 1] + [3, 2] + [100]
# .= [12] + [5] + [7] + [1] + [3] + [2] + [100]
#    .. intermediate steps..
#  = [1, 5, 7, 12] + [2, 3, 100] // processed subproblems
# 
# to do: result array elimination and time complexity analysis.
#
def merge_sorted_arrays(arr1, arr2):
    result  = []
    lenArr1 = len(arr1)
    lenArr2 = len(arr2)
    i,j     = 0, 0   
    while i < lenArr1 and j < lenArr2:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i = i+1
        else:
            result.append(arr2[j])
            j = j+1
    while i < lenArr1:
        result.append(arr1[i])
        i = i+1
    while j < lenArr2:
        result.append(arr2[j])
        j = j+1
    return result

def merge_sort(arr):
    n = len(arr)
    if n <=1:
        return arr
    first  = merge_sort(arr[0:(n//2)])
    second = merge_sort(arr[(n//2):])
    return merge_sorted_arrays(first, second)


## Quick sort
# [5, 23, 1, 6, 10, 3]
#  i                j
#
# [3, 23, 1, 6, 10, 5]
#      i            j
#
# [3, 5, 1, 6, 10, 23]
#     i  j
#
# [3, 1, 5, 6, 10, 23]
#       ij
#
# pivot = 5 
# [1, 5, 1, 6, 10, 5, 10]
#        j  i
#

def partition(arr):
    pivot = arr[0]
    i = 0
    j = len(arr) - 1
    while True:
        while arr[i] < pivot:
            i = i + 1
        while arr[j] > pivot:
            j = j - 1
        if i >=j:
            return j;# Do not return i here, it does not work for arrays of size 2       
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j - 1

def quick_sort(arr):
    n = len(arr)
    if n <=1:
        return arr
    part_index = partition(arr)
    first      = quick_sort(arr[0:part_index+1])    # [0:0] => empty
    second     = quick_sort(arr[part_index+1:])    # [0:2] => entire array 
    return first + second

#sort([1,2]) 
#pivot = 1
#part_index = 0
#[0, -1] = x
#[0, 1] = 


#sort(in) = [] + sort(in)

#=> sort[1] + sort[2] = [1,2]

#sort([1,2]) => sort[1] + sort[2] = [1,2]

#test  cases
def test_merge_sorted_arrays(in1_, in2_, out_):
    out = merge_sorted_arrays(in1_, in2_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)


def test_sort(in_,out_):
    out = merge_sort(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)
    out = quick_sort(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)

def test_partition(in_,out_):
    out = partition(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)
   

def run_tests():
    test_merge_sorted_arrays([1], [], [1])
    test_merge_sorted_arrays([], [1], [1])
    test_merge_sorted_arrays([1], [2], [1, 2])
    test_merge_sorted_arrays([2], [1], [1, 2])
    test_merge_sorted_arrays([1, 2], [3, 4], [1, 2, 3, 4])
    test_merge_sorted_arrays([1, 2, 3], [4], [1, 2, 3, 4])
    
#    test_merge_sort([], [])
    test_sort([1], [1])
    test_sort([1, 2], [1,2])
    test_sort([2, 1], [1,2])
    test_sort([3, 1, 2], [1, 2, 3])
    test_sort([3, 2, 1], [1, 2, 3])
    test_sort([2, 2, 1], [1, 2, 2])
    test_sort([3, 2, 1, 4], [1, 2, 3, 4])
    test_sort([3, 1, 1, 4], [1, 1, 3, 4])
    
    test_partition([1], 0)
    test_partition([1, 2], 0)
    test_partition([1, 2, 3], 0)
    test_partition([8, 1, 2, 3], 3)
    test_partition([5, 23, 1, 6, 10, 3], 2)
    
run_tests();
