class Solution(object):
  # O(n)
  def longestPalindrome(self, s):
    #check beforehand if the passed string is already a palindrome in itself
    #or if length of string is less than 3, then return s itself
    if (s==s[::-1] or len(s) < 3):
        return s
    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
        #check if "i" has crossed middle element and if length of largest 
        #palindrome till found, is greater than half of total length of string
        #then break, answer found no need to iterate more
        if (i>(len(s)//2) and len(res)>(len(s)//2)):
            break
    return res
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
  def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]
  def longestPalindrome1(self, s):
    """
    :type s: str
    :rtype: str
    """
    n=len(s)
    if n<2: return s
    start,maxlen,i=0,1,0
    while i<n:
      print("entering WHILE loop ")
      if n-i<=maxlen/2:
        break
      j,k=i,i
      while k<n-1 and s[k]==s[k+1]:   # ship the same character
	k = k+1
      i = k+1
      while k<n-1 and j>0 and s[k+1]==s[j-1]: #expand
        print("in while 2")
	k,j=k+1,j-1
      if maxlen<=k-j+1:
	print("in IF cond")
        start=j
        maxlen=k-j+1
    return s[start:start+maxlen] 
s = Solution()
a = "babad"
print(s.longestPalindrome1(a))
