# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/
# Given an array of strings, group anagrams together.
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
# ]
class Solution(object):
  def groupAnagram(self, input):
    dict_ = {}
    for item in input:
      key = " ".join(sorted(item))
      print("key ", key)
      if key not in dict_:
        dict_[key] = []
        print("dict in if::  ", dict_)
      dict_[key].append(item)   
      print("dict after append:: ", dict_)
    return dict_.values()
  
Input =  ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagram(Input))
