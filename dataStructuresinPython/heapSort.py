#	@SuGo, 7August 2018
#	Implementation of heap sort
#	Incorrect!
def heapSort(A):
	heapify(A)
	print("\n first heapify call made A as:: ", A, "\n")
	n = len(A)
	for i in range(n-1, 0, -1):
		(A[0], A[i]) = (A[i], A[0])
		print("for i=", i, "\n")
		print("A is:: ", A, "\n")
		heapify_(A, 0, i)
		print("after heapify_ ", i, "\n")
		print("A is::  ",A, "\n")
	print("Final and sorted array is:: ",A, "\n at i= ", i)
# 
def heapify(A):
	for i in range(int(len(A)/2), -1, -1):
		heapify_(A, i)
#
def heapify_(A, i, heapsize=None):
	heapsize = len(A)
	left = 2*i+1
	right =2*i+2
	if left<heapsize and A[left]>A[i]:
		largest = left
	else:
		largest = i
	if right<heapsize and A[right]>A[largest]:
		largest = right
	if largest!= i: 
		A[i],A[largest] = A[largest],A[i]
		heapify_(A, largest, heapsize)
#	**********
A = [6, 2, 7, 9, 3]
heapSort(A)
