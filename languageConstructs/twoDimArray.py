#	SuGo, 15 August 2018
#	creating a 2D array or list in python 
#	webref: https://snakify.org/en/lessons/two_dimensional_lists_arrays/


# define the number of rows and columns
rows = 3
cols = 4

# define the array
arr1D = [[0] * rows]
arr2D = [[0] * rows]*cols

print("1. [[0] * rows] := \t", arr1D) 
print("2. [[0] * rows]*cols := \t ", arr2D, "\n")
print("The problem with number 2. type declaration is that two lists will have the same ID number ie. they reference to the same list. Therefore, they do not represent a 2D array declration in python! \n Now Let's see a new way...")

# possible way 

arr1 = [0]*rows
for i in range(rows):
	arr1[i] = [0]*cols

print("2D array using new type of declaration\t", arr1, "\n") 

print("using append method ...\n")
arr2 = []
for i in range(rows):
	arr2.append([0]*cols)
print("for i in range(rows): \n \t arr2.append([0]*cols)\n", arr2, "\n")
# 	**** OR ***
print("using generator method ...\n")
arr3 = []
arr3 = [[0]*cols for i in range(rows)]
print("arr3 = [[0]*cols for i in range(rows)]\n ", arr3, "\n")
