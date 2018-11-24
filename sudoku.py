# not sure, if this solutions works
class Solution:
    def validSudoku(self, board):
      bigBoard = set()
      for i in range(0, 9):
        for j in range(0, 9):
          if board[i][j] != ".":
            curr = board[i][j]
            print("curr", curr)
            if (i, curr) in bigBoard or (curr, j) in bigBoard or (int(i/3), int(j/3), curr) in bigBoard:
              return False
            bigBoard.add((i, curr))
            bigBoard.add((curr, j))
            bigBoard.add((int(i/3), int(j/3), curr))
            print("bigBoard  ", bigBoard)
      return True

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

board2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
sol = Solution()
print(sol.validSudoku(board))
#print(sol.validSudoku(board2))
