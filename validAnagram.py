import collections
class Solution():
  def isAnagram(self, s, t):
    str1 = s
    str2 = t
    if len(str1) != len(str2):
      return False
    
    dictionary = {}
    for ind, item in enumerate(str1):
       if item not in dictionary:
        dictionary[item] = ind
    return dictionary
  
  def isAnagram2(self, s, t):
    return collections.Counter(s) == collections.Counter(t) if len(s) == len(t) else False
str1 = "bulbabcdijkhg"
str2 = "ulbbbcdakijgh"

s  =  Solution()
print(s.isAnagram2(str1, str2))
