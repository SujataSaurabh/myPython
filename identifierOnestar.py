def f(a,b):
	"this function is written to show the identifiers which can be used directly instead of passing arguments one by one"
	return a+b

## test function
c = (1, 2)
print("the result of addition of 1 and 2 is:: ", f(*c))
