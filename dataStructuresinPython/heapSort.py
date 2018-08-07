#	@SuGo, 7 August 2018
#	Implementation of heap sort

'''def heapSort(A):
	heapSize = len(A)
	# 
	for i in range(heapSize, -1, -1):
		heapify(A, heapSize, i)
	#
	for i in range(heapSize-1, 0, -1):
		A[i], A[0] = A[0], A[i]
		heapify(A, i, 0) 
	print(A)'''

def heapify(A, heapSize, i):
	largest = i
	left = 2*i+1
	right = 2*i+2
	if left<heapSize and A[left]>A[i]:
		largest = left 
	if right<heapSize and A[right]>A[largest]:
		largest = right
	if largest!=i: 
			A[i], A[largest] = A[largest], A[i]
			heapify(A, heapSize, largest)
#
def heapSort(A):
	heapSize = len(A)
	# 
	for i in range(heapSize, -1, -1):
		heapify(A, heapSize, i)
	#
	for i in range(heapSize-1, 0, -1):
		A[i], A[0] = A[0], A[i]
		heapify(A, i, 0) 
	print(A)
# 	********
A = [12, 11, 13, 5, 6, 7]
heapSort(A)
print("final array is::")
for i in range(len(A)):
	print("%d" %A[i])
