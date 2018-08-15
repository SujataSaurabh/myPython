#	SuGo, 14 August 2018
#	Square root of a number

def sqRootNo(number):
	number = float(number)
	return number**(1/2)

# 	test function
number = input("Enter the number to compute the square root:: ")
print("the square root of ",  number, " is ", sqRootNo(number))
print("\n the square root of the entered number is %f " %sqRootNo(number))
