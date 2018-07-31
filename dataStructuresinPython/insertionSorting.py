# @SuGo, 31 July 2018
# Insertion sorting algorithm
# In this sorting, every single value is compared with the rest of the values one by one. Hence, the complexity depends on the size of the input to be sorted. 
# Complexity::  Best case -- O(n) and Worst case -- O(n^2)
#
# -----------------
def insertionSort(A):
	xrange = range
	for i in xrange(1, len(A)):
		for j in xrange(i, 0, -1):
			if A[j]<A[j-1]:
				A[j], A[j-1] = A[j-1], A[j]
			else: break
	return A
# ------------------
A = [3, 5, 6, 1, 0, 9]
print(insertionSort(A))
