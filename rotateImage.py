class Solution():
  def rotateImage(self, matrix2D):
    """
    90 degree rotation is the 2 step procedure:
    1.  compute the transpose of the matrix
    2.  horizontal flip the transposed matrix
    """
    matrix2D = self.transpose(matrix2D)
    matrix2D = self.hFlip(matrix2D)
    return matrix2D
  
  def transpose(self, matrix2D):
    '''
    Since the matrix is 2D square, number of rows == number of columns
    '''
    rows = cols = len(matrix2D) 
    for i in range(0, rows):
      for j in range(0, i):
        matrix2D[i][j], matrix2D[j][i] = matrix2D[j][i], matrix2D[i][j]
    return matrix2D
  
  def hFlip(self, matrix2D):
    '''
    horizontal flipping
    '''
    rows = cols = len(matrix2D)
    for j in range(0, cols):
      for i in range(0, rows//2):
        matrix2D[j][i], matrix2D[j][rows-1-i] = matrix2D[j][rows-1-i], matrix2D[j][i] 
    return matrix2D
    
matrix2D = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

s = Solution()
print(s.rotateImage(matrix2D))
