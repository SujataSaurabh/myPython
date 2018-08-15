#	SuGo, 14 August 2018
#	Print square of a number

def squareNo(number):
	number = float(number)
	return str(number**2)

number  = input("Enter number to be squared:: ")
print("Square of ", number, "is:: ", squareNo(number))
