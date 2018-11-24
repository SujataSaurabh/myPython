# https://leetcode.com/problems/reshape-the-matrix/description/
class Solution(object):
  def reshapeMatrix(self, matRIX, Row, Col):
    flatten, out= [], []
    if len(matRIX)*len(matRIX[0]) == Row*Col:
      #flatten =[nums[r][c] for r in range(len(nums)) for c in range(len(nums[0]))]  
      for r in range(len(matRIX)):
        for c in range(len(matRIX[0])):
          print("r and c ", r, c)
          flatten.append(matRIX[r][c])
      print("flatten ", flatten)
      for r in range(Row):
        #
        print("flatten:: ", flatten[r*Col : r*Col+ Col])
        out.append(flatten[r*Col : r*Col+ Col])
      return out
    else:
      print("does not meet conditions!!")
      return matRIX
    
  
nums = [[1,2],[3,4]]
nums1 = [[1,2,3],[4,5,6],[7,8,9]]

s = Solution()
#print(s.reshapeMatrix(nums, 1, 4))
print(s.reshapeMatrix(nums1, 9, 1))
      
