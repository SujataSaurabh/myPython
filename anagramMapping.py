#	SuGo, 23 August 2018
# https://leetcode.com/problems/find-anagram-mappings/description/
# Example ::
#	A = [12, 28, 46, 32, 50]
#	B = [50, 12, 32, 46, 28]
#result: [1, 4, 3, 2, 0]	
# time and space complexity: O(n)
import collections
class Solution:
	def anagramMapping(self, A, B):
		lookup = collections.defaultdict(collections.deque)
		for index, item in enumerate(B):
			lookup[item].append(index)
		result = []
		for item in A:
			result.append(lookup[item].popleft())
		return result

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
C = [40, 40]
D = [40, 40]
sol = Solution()
print(sol.anagramMapping(A, B))
print(sol.anagramMapping(C, D))
