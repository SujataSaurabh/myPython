# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/
class Solution(object):
  def tripletSubseq(self, A):
    # fails for 1 input [5, 1, 5, 5, 2, 5, 4]
    # refer ot implementation 2 for the perfect answer
    n = len(A)
    f = False
    if n<3: return 
    for i in range(n-3):
      if A[i]<A[i+1]:
        if A[i+1]<A[i+2]:
          f = True
    if A[-3]<=A[-2]<=A[-1]:
        f = True
    return f
  # implementation 2 
  def increasingTriplet(self, nums):
    # perfect and the submitted implementation 
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        minval=nums[0]
        find=0
        mid=nums[0]
        for num in nums[1:]:
            if find and num>mid:
                return True
            elif find and num>minval:
                mid=num
            elif find:
                minval=num
            else:
                if num>minval:
                    find=1
                    mid=num
                else:
                    minval=num
        return False

A = [1,2,3,4,5]
B = [5,4,3,2,1]
C = [2,1,5,0,4,6]
D = [1]
E = [5,1,5,5,2,5,4]

s = Solution()
print(s.tripletSubseq(A))
print(s.tripletSubseq(B))
print(s.tripletSubseq(C))
print(s.tripletSubseq(D))
print(s.tripletSubseq(E))
print(s.increasingTriplet(E))
