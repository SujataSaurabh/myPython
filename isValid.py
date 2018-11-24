class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openBrackets = ["(", "[", "{"]
        closeBrackets = [")", "]", "}"]
        stack = []
        for brackets in s:
            if brackets in openBrackets:
                brack_id = openBrackets.index(brackets)
                stack.append(closeBrackets[brack_id])
            elif brackets in closeBrackets:
                if len(stack)==0:
                    return False
                item = stack.pop()
                if item != brackets:
                    return False
        return True

s = "(]"
sol = Solution()
print(sol.isValid(s))
