# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: nums = [3, 6, 1, 0]
        Output: 1
        Explanation: 6 is the largest integer, and for every other number in the array x,
                     6 is more than twice as big as x.  The index of value 6 is 1, so we                          return 1.
        Input: nums = [1, 2, 3, 4]
        Output: -1
        Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
        
        """
        maxNumber = max(nums)
        for i in range(len(nums)):
            print("i ", i)
            if maxNumber == nums[i]:
                print("max",  maxNumber, "nums[i]", nums[i])
                continue
            if maxNumber < 2*nums[i]:
                print("i ", i, nums[i], 2*nums[i])
                print(maxNumber,  " >= ",  2*nums[i])
                return -1
        return nums.index(maxNumber)
    
nums = [1, 2, 3, 4]
s = Solution()
print(s.dominantIndex(nums))
