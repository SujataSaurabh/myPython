#https://leetcode.com/problems/two-sum/description/
# best run time
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # sort the given array
        sorted_nums = sorted(nums)
        # take two indices i,j
        i = 0 #start
        j = len(sorted_nums)-1 #end
        
        s = sorted_nums[i]+sorted_nums[j] 
        while s != target:
            # move j to left if sum > target (to decrease sum) 
            if s > target:
                j-=1
            else:
                i+=1 # move i to right if sum < target (to increase sum)
            s = sorted_nums[i]+sorted_nums[j]
        # return corresponding indices of elements in original array
        x = nums.index(sorted_nums[i])
        # change value at x to avoid referring to same element twice
        nums[x] = -1
        y = nums.index(sorted_nums[j])
        return [x,y]
      
    def twosum(self, nums, target):
        dict_ = {}
        for i in range(len(nums)-1):
          if item in dict_:
            return [dict_[item]]
          else:
            dict_[target - item]
        
