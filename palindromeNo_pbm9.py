#	SuGo, 25 August 2018
#	https://leetcode.com/problems/palindrome-number/description/
#  Example:Input: 121
#	    Output: true
#  Example: Input: -121
#	    Output: false

class Solution:
	def palindrome(self, InputStr):
		"""
		Checks for the palindrome by converting the input into a string
		"""
		InputStr = str(InputStr)
		if InputStr[0:] == InputStr[::-1]:
			return True
		else:
			return False

	def palindromeInt(self, inputInt):
		"""
		finds a number palindrome without converting it into a string.
		"""
		if inputInt < 0:
			return 
		copy, reverse = inputInt, 0
		while copy:
			reverse = reverse*10
			reverse = reverse + copy%10
			copy    = copy//10
		return (inputInt==reverse)
inputStr = 12121
sol = Solution()
print(sol.palindrome(inputStr))
print(sol.palindromeInt(inputStr))
