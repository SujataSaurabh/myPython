#	SuGo, 14 August 2018
#	This program prints the area of a circle

def areaCircle(radius):
	radius = float(radius) 	# data type conversion
	pi     = 3.14
	return pi*(radius**2)

# 	test function
radius = input("Enter the radius of the circle:: ")
print("Area of the circle with radius ", radius, " is ", areaCircle(radius), "unit squared.")
