#	@SuGo, 3 August 2018
#	Implementation of the Binary search algorithm
#	Complexity: O(log n)
def binSear(A, ele_to_search):
	initialPos = 0
	lenArr     = len(A)-1
	while initialPos<=lenArr:
		mid = int((initialPos+lenArr)/2)
		if ele_to_search<A[mid]:
			lenArr = mid-1
		elif ele_to_search>A[mid]:
			initialPos = mid+1
		else: 
			return mid
	return None
# --------- test the algorithm --------
A = [5, 10, 12, 15]
ele_to_search = 10
print("Binary search found out the element 10 at_  ", binSear(A, ele_to_search), "  _position")
