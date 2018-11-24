# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727
# Algorithm steps:
#             1. start scanning the array from 0 to end element 
#             2. Take an extra counter pointing to the nextInd location
#             3. This counter increments only if a different element is encountered, 
#                 else it stays same 
#             4. Lastly, check if the value of the counter and scanned index "i" is the
#                 same. If same that means, non-identical elements are on adjacent position. 
#                 IF NOT, then we have to shift the duplicate element to the end of the array
#             5. Return the counter value incremented by 1, as it started from 0th index         
class Solution():
  def removeDuplicates(self, A):
    lengthA = len(A)
    nextInd = 0
    
    for i in range(0, lengthA):
      if A[i] != A[nextInd]:
        nextInd = nextInd+1
        if i!= nextInd:
          A[nextInd] = A[i]
    return nextInd+1
  
A = [1, 1, 2]
s = Solution()
print(s.removeDuplicates(A))
  
