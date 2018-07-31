def memoize(f):
	memo = {}
	def helper(x):
		if x not in memo:
			memo[x] = f(x)
		return memo[x]
	return helper
@memoize
def fib(n):
	return n if n<2 else fib(n-1)+fib(n-2)
# now test the function 
#fib = memoize(fib)
print("The fibonacci number 11 retuns:: ", fib(11))
