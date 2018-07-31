def f(a, b):
	"This program shows the double star type identifier which can be used to refer to the input arguments passed to a function"
	return (a+b)
## test the function
c ={'a':1,'b':2}
print("Printing the result of {'a':1,'b':2}:: ", f(**c)) 
