# https://leetcode.com/problems/3sum/description/
# Example: input  A = [-1, 0, 1, 2, -1, 4]
#          output A = [[-1, 0, 1], [-1, -1, 2]]

class Solution(object):
  def threeSum(self, A):
    # step 1 : sort
    A.sort()
    result = []
    n      = len(A)
    for i in range(0, len(A)-2):
      if i>0 and A[i] == A[i-1]:
        print("i>0 and A[i] == A[i-1] ", i)
        continue
# continue statement stops the executionof the remaining statement and moves the control back to the begining of the loop
      print("After continue i = ", i)
      left = i+1
      right = len(A)-1
      while(left<right):
        print("left ", left)
        if(A[i] + A[left] + A[right])>0:
          print("A[i] + A[left] + A[right] ", A[i] + A[left] + A[right])
          right -=1
        elif (A[i] + A[left] + A[right])<0:
          print("A[i] + A[left] + A[right] ", A[i] + A[left] + A[right])
          left +=1
        else:
          if (left >(i+1)) and (A[left] == A[left-1]):
            print("left ", left, " and i+1 ", (i+1))
            left +=1
            continue
          result.append([A[i], A[left], A[right]])
          left +=1
          print("last left ", left)
    return result
 #  Second implementation of three sum (threeSum1) and four sum (using three sum)  
  def threeSum2(self, nums):
        res = []
        #nums = sorted(nums)
        nums.sort()  
        
        for i in range(len(nums) -2 ):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            e = nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                s = e + nums[l] + nums[r]
                if s<0:
                    l += 1
                elif s>0:
                    r -= 1
                
                else: #if s == 0:
                    res.append([e, nums[l], nums[r]] )
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
  def threeSum1(self, nums, target):
      results = []
      nums.sort()
      for i in range(len(nums)-2):
        l = i + 1; r = len(nums) - 1
        t = target - nums[i]
        if i == 0 or nums[i] != nums[i-1]:
          while l < r:
            s = nums[l] + nums[r]
            if s == t:
              results.append([nums[i], nums[l], nums[r]])
              while l < r and nums[l] == nums[l+1]: l += 1
              while l < r and nums[r] == nums[r-1]: r -= 1
              l += 1; r -=1
            elif s < t:
              l += 1
            else:
              r -= 1
      return results

  def fourSum(self, nums, target):
    results = []
    nums.sort()
    for i in range(len(nums)-3):
      if i == 0 or nums[i] != nums[i-1]:
        threeResult = self.threeSum1(nums[i+1:], target-nums[i])
        print("threeResult ", threeResult)
        for item in threeResult:
          print("item - ", item)
          results.append([nums[i]] + item)
    return results
  
A = [-1, 0, 1, 2, -1, -4]
B = [4,-1,-1,0,1,2]
s = Solution()
print(s.threeSum(A))
print(s.threeSum1(A, 0))
print("THREE SUM 2")
print(s.threeSum2(B))
print("four sum", s.fourSum(A, 0))
      

