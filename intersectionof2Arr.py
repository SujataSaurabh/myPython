import collections
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = list(set(nums1)) 
        b = list(set(nums2))
        c = list(set(nums1).intersection(set(nums2)))
        return c
    def intersectionII(self, nums1, nums2):
      '''
      Given two arrays, write a function to compute their intersection.
        Example 1: Input: nums1 = [1,2,2,1], nums2 = [2,2]
                Output: [2,2]
      '''
      res = []
      for item in nums1:
          if item in nums2:
            res.append(item)
            nums2.remove(item)
      return res 
    
    def intersectII_counter(self, nums1, nums2):
        c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
        for num in c1 and c2:
         # return ([num] *  min(c1[num], c2[num]))
          return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])
    

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
s = Solution()
print(s.intersection(nums1, nums2))
A = [1, 2, 2, 1, 1, 3, 4]
B = [2, 2]
print(s.intersectII_counter(nums1, nums2))
