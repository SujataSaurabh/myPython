# Spiral matrix
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        
        1. Input:
            [
                [ 1, 2, 3 ],
                [ 4, 5, 6 ],
                [ 7, 8, 9 ]
            ]
        Output: [1,2,3,6,9,8,7,4,5]
        2. Input:
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9,10,11,12]
            ]
        Output: [1,2,3,4,8,12,11,10,9,5,6,7]
        Idea:
        while matrix is not null
        1. remove the first line of the matrix, and extend the list to  result
        2. rotate the matrix counterclockwisely
        """
        res = []
        while matrix:
            res.extend(matrix[0])
            print("res",res )
            matrix.remove(matrix[0])
            # 2. rotate the matrix counterclckwise
            matrix = list(zip(*matrix))[::-1]
            print(matrix)
        return res
            
s = Solution()
matrix = [
                [ 1, 2, 3 ],
                [ 4, 5, 6 ],
                [ 7, 8, 9 ]
            ]
print(s.spiralOrder(matrix))
