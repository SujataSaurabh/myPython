#	@SuGo, 5 August, 2018
#	Quick sort implementing by taking the last element as Pivot
#	ref: https://www.geeksforgeeks.org/quick-sort/
#	time complexity:: worst case -- O(n^2); best and average case -- O(nlog(n))
def partition(A, p, q):
	i = p-1
	pivot = A[q]
	for j in range(p, q):
		if A[j]<=pivot:
			i = i+1
			A[i], A[j] = A[j], A[i]

	A[i+1], A[q] = A[q], A[i+1]
	return (i+1)
#
def quickS(A, p, q):
	if(p<q):
		pivotPos = partition(A, p, q)
		print("Pivotpos and element:: ", pivotPos, " and ",A[pivotPos], "\n")
		print("Array: ", A, "\n")
		quickS(A, p, pivotPos-1)
		quickS(A, pivotPos+1, q)
#
A = [10, 5, 4, 0, 9]
print("Original array:: ",A)
p = 0
q = len(A)-1
print("Sorted array:: ", quickS(A, p, q))

