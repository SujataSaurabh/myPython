#   This page contains follwoing sorting algos
# 1. insertion, 2. quick, 3. merge, 4. heap sort, 5. bucket, 6. bubble, 7. selection
# ####
import time
start_time = time.clock()
# ####
def insertion(arr):
  '''
  algo: loop from i = 1 to (n-1)
        pick an element a[i] and insert it into the sorted sequence a[0..(i-1)]
        time complexity:
          best case:              O(n)
          average and worst case: O(n^2)
        worst case space complexity: O(n) total, O(1) auxiliary      '''
  i = 1
  while i < len(arr):
    x = arr[i]
    j = i-1
    while j>=0 and arr[j]>x:
      arr[j+1] = arr[j]
      j        = j-1
    arr[j+1]   = x
    i   += 1
  return arr
print(time.clock() - start_time, "seconds (insertion)")
#
def bubble(arr):
  '''
  time complexity:
  worst and average: O(n^2)
  best:              O(n)
  space complexity:  O(1)
  '''
  n = len(arr)
  swap  = True
  while not swap:
    swap = False
    for i in range(1, n-1):
      if arr[i-1]>arr[i]:
        arr[i-1] = arr[i]
        swap = True
    n -=1
  return arr
print(time.clock() - start_time, "seconds (bubble)")    
#
def selection(arr):
  '''
  divide the list into two such that one half list is sorted. 
  example: arr = (11, 25, 12, 22, 64)
  Sorted sublist == ( )
  Unsorted sublist == (11, 25, 12, 22, 64)
  Least element in unsorted list == 11

  Sorted sublist ==  (11)
  Unsorted sublist == (25, 12, 22, 64)
  Least element in unsorted list == 12

  Sorted sublist == (11, 12)
  Unsorted sublist == (25, 22, 64)
  Least element in unsorted list == 22 and so on...
  
  time complexity:
    worst, base and average case : O(n^2)
    with O(n) swaps
  space complexity:
    O(1) auxiliary
  '''
  for i in range(0, len(arr)-1):
    minimum = i
    for j in range(i+1, len(arr)):
      if arr[j]<arr[minimum]:
        minimum = j 
    if i!= minimum:
      arr[i] = arr[minimum]
  return arr
print(time.clock() - start_time, "seconds (selection) \n \n")    
#  
def bucket(alist):
    '''
    time complexity:
      worst - O(n^2)
      best and average - o(n+k)
    space complexity: O(n.k)     
    '''
    largest = max(alist)
    length  = len(alist)
    size    = largest/length
    buckets = [[] for _ in range(length)]
    #print("buckets, largets and length, size ", buckets, largest, length, size)
    for i in range(length):
        j = int(alist[i]/size)
        print("j1 ", j)
        if j != length:
            print("j2 ", j)
            buckets[j].append(alist[i])
            print("bukcet1 ", buckets)
        else:
            buckets[length - 1].append(alist[i])
            print("bukcet2 ", buckets)
    for i in range(length):
        insertion(buckets[i])
    result = []
    for i in range(length):
        result = result + buckets[i]
    return result
print(time.clock() - start_time, "seconds (bucket) \n \n")    
#  
#   **part I**
def mergeSort(arr, p, r=0):
  '''
  time complexity: 
      worst, best and average case: O(n log(n))
  space complexity:
    O(n) total with O(n) auxiliary
  '''
  if r == 0:
    r = len(arr)
  while p<(r-1):
    q = int((p+r)/2)
    mergeSort(arr, p, q)
    mergeSort(arr, q, r)
    merge(arr, p, q, r)
# **part II**
def merge(arr, p, q, r):
  B, i, j = [], p, q
  while True:
    if arr[i]<=arr[j]:
      B.append(arr[i])
      i+=1
    else:
      B.append(arr[j])
      j+=1
    if i==q:
      while j<r:
        B.append(arr[j])
        j+=1
      break
    if j==r:
      while i<q:
        B.append(arr[i])
        i+=1
      break
  arr[p:r] = B
print(time.clock() - start_time, "seconds (merge) \n \n")    
#      
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
print(" ******  RESULTS  ******")
arr = [12, 11, 6, 13, 5, 6] 
arr1 = [5, 6, 11, 12, 13]
#print("insertion on an unsorted array \n", insertion(arr)) 
#print("insertion on a sorted array \n", insertion(arr1)) 
#print("bubble \n", bubble(arr))
#print("selection \n", selection(arr))
#print("bucket \n", bucket(arr))
print("merge \n", quickS(arr, 0, len(arr)-1))
print("     ******    ****** \n\n")
print(time.clock() - start_time, "seconds (total)")
