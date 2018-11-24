class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_  = {}
        length =  0
        for i in s:
          if i not in dict_:
            print(i)
            dict_[i] = 1
            length +=1
          else:
            dict_[i] = dict_[i]-1 
            print("2 ", i)
        return length
s = "abba"
s1 = Solution()
print(s1.lengthOfLongestSubstring(s))
