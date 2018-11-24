nums = [-1,-1,-1,0,1,1] 
#[-1,-1,-1,-1,0,1]
 

class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        1. index = -1
        2. from index = 2 to end of array
            s1  = sum(array[::index])
            s2  = sum(array[index::])
            if s1 == s2:
                return index
           return -1
            
        """
        indx = -1
        print("length ", len(nums))
        for i in range(0,len(nums),1):
            print("1--", i, nums[i])
            sumLeft  = sum(nums[:(i)])
            print("left: ", sumLeft, " numsL -- ", nums[:(i)])
            sumRight = sum(nums[(i+1):])
            print("right: ", sumRight," numsR -- ", nums[(i+1):])
            if sumLeft == sumRight:
                return i
        return indx
    #
    def pivotIndex2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        1. index = -1
        2. from index = 2 to end of array
            s1  = sum(array[::index])
            s2  = sum(array[index::])
            if s1 == s2:
                return index
           return -1
            
        """
        indx = -1
        sL = 0
        sR = sum(nums)
        print("length ", len(nums))
        for i in range(len(nums)):
            sR-= nums[i]
            if sL == sR:
                return i
            sL += nums[i]
        return indx

s = Solution()
print(s.pivotIndex(nums))
