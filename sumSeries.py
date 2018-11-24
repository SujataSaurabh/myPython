class Solution(object):
  def twoSum(self, A, target):
    for i in range(0, len(A)):
      if (target-A[i]) in A[i+1:]:
        print(i, A.index(target-A[i]))
        return [i, A.index(target-A[i], i+1, len(A))]
      
  def threeSum(self, nums):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(0, n-2):
      a = nums[i]
      start = i+1
      end = n-1
      while (start < end):
        b = nums[start]
        c = nums[end]
        if a+b+c == 0:
          res.append([a, b, c])
        # Continue search for all triplet combinations summing to zero.
        # We need to update both end and start together since the array values are distinct.
          start = start + 1
          end = end - 1
        elif a+b+c > 0:
            end = end - 1
        else:
            start = start + 1
      return res
    
  def fourSum(self, nums, target):
        result = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                head_1= j+1
                tail_1 = len(nums)-1
                while tail_1 > head_1:
                    sum_sum = nums[i] + nums[j] + nums[head_1] + nums[tail_1]
                    if sum_sum > target:
                        tail_1-=1
                    elif sum_sum < target:
                        head_1+=1
                    else:
                        if [nums[i], nums[j] , nums[head_1] ,nums[tail_1]] not in result:
                            result.append([nums[i], nums[j] , nums[head_1] ,nums[tail_1]])
                        tail_1-=1
                        head_1 += 1
        return result
    #     --- Recursively approached (Best approach!) ---
  def foursum(self, nums, target):
    nums.sort()
    results = []
    self.findNsum(nums, target, 4, [], results)
    return results
  
  def findNsum(self, nums, target, N, result, results):
    if len(nums) < N or N < 2: return
    # solve 2-sum
    if N == 2:
        l,r = 0,len(nums)-1
        while l < r:
            if nums[l] + nums[r] == target:
                results.append(result + [nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while r > l and nums[r] == nums[r + 1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(0, len(nums)-N+1):   # careful about range
            if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                break
            if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
    return
  
  def threesum(self, nums, target):
    nums.sort()
    results = []
    self.findNsum(nums, target, 3, [], results)
    return results
  
A = [2, 7, 12, 15]
target = 27
s =Solution()
#print(s.twoSum(A, target))
B  = [-1, 0, 1, 2, -1, -4]
print(s.threesum(B, 0))
#B.sort()
#print(B)
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(s.fourSum(nums, target))
print(s.foursum(nums, target))
