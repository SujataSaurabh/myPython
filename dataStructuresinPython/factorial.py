def factorial(n):
	if n==0:
		return 1
	else: 
		return (n*factorial(n-1))
# test the function "FACTORIAL"
f = factorial(21)
print("\n Factorial of 21 is: ", f, "\n")
print("Factorial of 4 is: ", factorial(4))
