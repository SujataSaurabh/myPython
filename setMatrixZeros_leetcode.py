# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
# https://leetcode.com/problems/set-matrix-zeroes/discuss/26115/JavaPython-O(1)-space-11-lines-solution
#
#Input: 
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
#Output: 
#[[1,0,1],
#  [0,0,0],
#  [1,0,1]]
#
class Solution(object):
  # imolementation 1
  def matrixZeros(self, matrix):
    rowFlag = False
    colFlag = False
    rows    = len(matrix)-1
    cols    = len(matrix[0])-1
    print("rows and cols ", rows,cols)
    
    for i in range(0, rows):
      for j in range(0, cols):
        if i == 0 and matrix[i][j] == 0:
          print("i ", i)
          rowFlag = True
        if j == 0 and matrix[i][j] == 0:
          print("j ", j)
          colFlag = True
        if matrix[i][j] == 0:
          print("i and j", i, j)
          matrix[0][j] = 0
          matrix[i][0] = 0
    
    for i in range(0, rows):
      for j in range(0, cols):
        if matrix[0][j] == 0 or matrix[i][0] == 0:
          print("i and j 2 -- ", i, j)
          matrix[i][j] = 0
          
    if rowFlag == True:
      for i in range(0, cols):
        print("cols ", i)
        matrix[0][cols] = 0
      
    if colFlag == True:
      for i in range(0, rows):
        print("rows ", i)
        matrix[rows][0] = 0
    return matrix
  # using set()
  # O(m*n) time complexity
  def matrixZeros_(self, matrix):
    rowID = set()
    colID = set()
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(0, rows):
      for j in range(0, cols):
        if matrix[i][j] == 0:
          rowID.add(i)
          colID.add(j)
          
    for i in range(0, rows):
      for j in range(0, cols):
        if i in rowID or j in colID:
          matrix[i][j] =0
    return matrix

  def setZeroes(self, matrix):
    rows = set()
    columns = set()       
        #First pass to check which rows and columns will need to be changed
    for y in range(len(matrix)):
      for x in range(len(matrix[0])):
        if matrix[y][x] == 0:
          rows.add(y)
          columns.add(x)      
        #Second pass to change rows and columns to zero values
    for y in range(len(matrix)):
      for x in range(len(matrix[0])):
        if y in rows or x in columns:
          matrix[y][x] = 0
    return matrix
    #######  
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
matrix_ = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5], 
  [1, 2, 0, 0]
]

s = Solution()
print(s.setZeroes(matrix_))
#print(s.matrixZeros1(matrix_))
    
