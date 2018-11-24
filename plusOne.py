# https://leetcode.com/problems/plus-one/description/
class Solution(object):
  def plusOne(self, Arr):
    lastInd = len(Arr) - 1
    A[lastInd] = A[lastInd] + 1
    if A[lastInd]>9: # does this only if last element is 10, improves the run time of code
      carry = 0
      while lastInd>=0:
        newLastIndex = A[lastInd] + carry
        A[lastInd]   = newLastIndex%10
        carry        = int(newLastIndex/10)
        lastInd     -= 1
      if carry >0:
        A.insert(0, carry)
    return A

A = [1, 2, 9]
s = Solution()
print(s.plusOne(A))
