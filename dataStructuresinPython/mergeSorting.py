# @SuGo, 31 July 2018
# Merge sort. Complexity -- O(nlog(n))
# 
def mergeSort(A, p, r=0):
	"Merge Sort:: Sorts an unsorted array by decomposing it to the level of individual values. Then the decomposed values are sorted and merged together. "
	if r==0:
		r=len(A)
	if p<(r-1):
		q = int((p+r)/2)
		mergeSort(A, p, q)
		mergeSort(A, q, r)
		merge(A, p, q, r)
#
def merge(A, p, q, r):
	B, i, j = [], p, q
	while True:
		if(A[i]<=A[j]):
			B.append(A[i])
			i = i+1
		else:
			B.append(A[j])
			j = j+1
		if(i==q):
			while j<r:
				B.append(A[j])
				j = j+1
			break
		if(j==r):
			while i<q:
				B.append(A[i])
				i = i+1
			break
	A[p:r] = B
	print("Array A after sort is ::",  A, "\n")
# Test the functions
A = [4, 3, 5, 8, 2, 0, 21, 114, 10]
print("ORIGINAL ARRAY IS :: ", A, "\n")
print("APPLYING MERGE SORT ON THE ARRAY ... \n")
mergeSort(A, 0)
