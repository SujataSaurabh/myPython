#https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
import collections
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        Input:
        [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ]

        Output:  [1,2,4,7,5,3,6,8,9]
        explanation:
                [a11, a12, a13],
                [a21, a22, a23], 
                [a31, a32, a33]
                sum of the indices along the required diagonal order are all equal, see                       below:
                1+2 = 2+1 
                1+3 = 2+2 = 3+1
                2+3 = 3+2
                3+3
                
                output = [1,2,4,7,5,3,6,8,9]
                    i  =  0,1,2,3,4,5,6,7,8 
                use dictionary to maintain the odd and even indices sum
        """
        dic    = collections.defaultdict(list)
        result = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                print(matrix[i][j])
                dic[i+j+1].append(matrix[i][j])
        for i in dic.keys():           
            if i%2 == 1:
                dic[i].reverse()
            result+=dic[i]
        return result
     
s = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

s.findDiagonalOrder(matrix)
        
