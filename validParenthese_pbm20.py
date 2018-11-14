#	SuGo, 25 August 2018
#	https://leetcode.com/problems/valid-parentheses/description/
#
class Solution:
	def validParenthesis(self, parenthese):
		openBrackets = ["(", "[", "{"]
		closeBrackets = [")", "]", "}"]
		stack = []
		for brackets in parenthese:
			if brackets in openBrackets:
				brack_id = openBrackets.index(brackets)
				stack.append(closeBrackets[brack_id])
			elif brackets in closeBrackets:
				item = stack.pop()
				if item != brackets:
					return False
		return True
	def isValid(self, parenthese):
		dict_ = {"(":")", "[":"]", "{":"}"} 
		stack = []
		for bracket in parenthese:
			if bracket in dict_:
				stack.append(bracket)
			elif bracket != dict_[stack.pop()]:
				return False
		return len(stack) == 0	
s = "[}"
sol = Solution()
print(sol.validParenthesis(s))
print(sol.isValid(s))
