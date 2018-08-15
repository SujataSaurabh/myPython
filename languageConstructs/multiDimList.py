#	SuGo, 15 August 2018
#	creating a 2D list or 2D array

# for example a matrix defining the seat availability of a cinema hall 

cinema = []
print("cinema", cinema)
for j in range(5):
	column = []
	print("1st column ", cinema)
	for i in range(5):
		column.append(0)
		print("i and j column", column)
	cinema.append(column)
print("cinema final ", cinema)

#multDlist = [][]
#print(multDlist)
