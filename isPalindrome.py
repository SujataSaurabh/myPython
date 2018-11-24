class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        print("s" , s[:])
        print("reverse s ", s[::-1])
        return True if s[:] == s[::-1] else False
      
s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))
