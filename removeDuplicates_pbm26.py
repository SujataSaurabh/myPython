#	SuGo, 25 August 2018
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nextInd = 0
        if len(nums)==0:
          return 0
        for i in range(0, len(nums)):
          if nums[i]!= nums[nextInd]:
            nextInd  = nextInd+1
            if i!=nextInd:
              nums[nextInd] = nums[i]
        return  nextInd+1 
      
nums = [1, 1, 2]
s = Solution()
print(s.removeDuplicates(nums))
