#	@SuGo, 5 August 2018
#	Implementation of min heap using "heapq" class already implemented in python
#	and tesing the push and pop functions
#	--------------
from heapq import heappop, heappush
a = [6, 2, 7, 8, 9]
print("Original array:: ", a, "\n")
heap = []
for element in a:
	heappush(heap, element)
print("Heap implementation:: \n")
while heap:
	print(heappop(heap))
