# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646

class Solution():
  def rotate(self, nums, k):
    # check if the number of rotations are divisible by the length of the array
    # if remainder is 0 that means the rotated array will be the same 
    k = k%len(nums)
    if k!=0:
      nums[:] = nums[-k:] + nums[:len(nums)-k]
      print(nums)
    else:
      print(nums)
    
    
A = [1, 2, 3, 4,5, 6, 7]
s =Solution()
s.rotate(A, 5)
