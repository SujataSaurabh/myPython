# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
class Solution():
  def containsDuplicate(self, nums):
    # return True if the array contains any duplicates else False
    return True if len(nums)!= len(set(nums))  else False
  
nums = [1,2,3,1]
s = Solution()
print(s.containsDuplicate(nums))
