# Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]
class Solution(object):
  def findmissingRange(self, nums, lower, upper):
    result = []
    nums = [lower-1] + nums + [upper+1]
    print(nums)
    for i in range(len(nums)- 1):
      if not nums[i]+1 >= nums[i+1]:
        if nums[i+1]== nums[i] +2:
          result.append(str(nums[i] +1))
        else:
          result.append(str(nums[i] +1)+'->'+str(nums[i+1] - 1))
    return result
  def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        nums = [lower-1]+nums+[upper+1]
        print(nums)
        for i in range(len(nums)-1):
            print("i ", i)
            if not nums[i+1] <= nums[i]+1:
                print("if not cond ", nums[i+1],"and",  nums[i]+1 )
                if nums[i+1] == nums[i]+2:
                    print("if cond ", nums[i+1],"and",  nums[i]+2 )
                    res.append(str(nums[i]+1))
                else:
                    print("else cond ", nums[i]+1,"and",  nums[i+1]-1 )
                    res.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))
        return res
  def missingRange(self, A, lower, upper):
    # fails for some cases
    n = len(A)
    out = []
    if nums == []:
          s = lower
          u = upper
          if s == u:
            out.append(str(u))
          else:
            out.append(str(s)+'->'+str(u))
    else:
      for i in range(0, n-1):
        j = i+1
        print("I am here", A[j] - A[i])
        if (A[j] - A[i]) >1:
          print("yes, cond 1 !")
          start = A[i]+1
          end   = A[j]-1
          if start ==end:
            print("start == end")
            out.append(str([start]).strip('[]'))
          else:
            print("no they are not equal")
            out.append(str([start, end]).strip('[]'))
        else:
          print("Nothing satisfied!")
        #return
      if A[-1] != upper:
        out.append(str([A[-1]+1, upper]).strip('[]'))
    return out
  
nums = [0, 1, 3, 50, 75]
lower = 0 
upper = 99
nums1 = [-1]
l = -2
u = -1
s =Solution()
print(s.findMissingRanges(nums, lower, upper))
#print(s.findMissingRanges(nums1, l, u))        
  
