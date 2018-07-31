# Memoization using the Fibonacci series
#@ SuGo, 31 July 2018
class Memoize:
	"Memoization is used to save the information in the memory so that it can be used later by the program. This strategy save the computation time and speeds up the program performance."
	def __init__(self, fn):
		self.fn = fn
		self.memo = {}
	def __call__(self, *args):
		if args not in self.memo:
			self.memo[args] = self.fn(*args)
		return self.memo[args]
@Memoize
def fib(n):	
	return n if n<2 else fib(n-1)+fib(n-2)
#
print("The Fibonacci number 11 returns:: ", fib(11))
