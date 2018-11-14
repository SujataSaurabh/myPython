#	SuGo, 24 August 2018
#	https://leetcode.com/problems/two-sum/description/

class Solution:
	def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
	time complexity : O(n^2)
        """
        result = []
        for i in range(len(nums)):
            for j in range((i+1), len(nums)):
                    if (nums[i] + nums[j] == target):
                        result.append(i)
                        result.append(j)
        return result
#		****  Implementation 2 	****	
	def twoSum2(self, nums, target):
		"""
		Time complexity: O(n)
		Space : 	 O(n)
		"""
		



nums = [2, 7, 11, 15]
target = 9
solve  = Solution()
print(solve.twoSum(nums, target))
