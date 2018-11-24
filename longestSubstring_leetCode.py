# Longest Substring Without Repeating Characters
# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
class Solution(object):
  # O(n) time 
  def longestSubstring(self, strInp):
    dict_  = {}
    start  = 0
    maxLen = 0
    for i,c in enumerate(strInp):
            print("i and c ", i, c)
            if(c not in dict_ or dict_[c]<start):
                print("dict[c] ", dict_)
                maxLen = max(maxLen,1+i-start)
                print("1+i-start = ", (1+i-start))
            else:
                start = dict_[c]+1
                print("start = ", start)
            dict_[c] = i
            print("dict_[c] = ", dict_[c])
    return maxLen

a =  'abcabcbb'
b =  'bbbbb'
c =  'pwwkew'
s = Solution()
print(s.longestSubstring(a))
#print(s.longestSubstring(b))
#print(s.longestSubstring(c))
