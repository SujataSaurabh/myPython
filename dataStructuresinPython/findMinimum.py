#@SuGo, 31 July 2018
#
def findMinimum(A):
	minValue = A[0]
	for eachValue in A:
		if eachValue<minValue:
			minValue = eachValue
	return minValue
# test the function
A = [15,-16, 18, 0, 12, 2, 3, 4, 5]
print("The original array is:: ", A, "\n")
print("Minimum value in the array is:: ", findMinimum(A), "\n")
