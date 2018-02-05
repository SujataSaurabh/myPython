#My First Program to start with Python
# Source: https://learnpythonthehardway.org/python3/
#print("hello")
#print("I am Sujata Goswami")
#print(3 +2 < 5-4)
cars         = 100
space_in_car = 4
drivers      = 30
passengers   = 90
cars_not_driven = cars - drivers
cars_driven     =  drivers
carpool_capacity = cars_driven * space_in_car
avgPassengerperCar = passengers/cars_driven

print("all the required variables.")
print("There are", cars, "cars available.")
print("There are only", drivers, "available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put", avgPassengerperCar, "in each car.")
