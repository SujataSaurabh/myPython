# Here is the lesson to learn the lists data structure in python
# source -- https://docs.python.org/3/tutorial/introduction.html#lists
# SuGo

listOfSquares = [1, 4, 9, 16, 25]
print("list of squares of numbers up to 5", listOfSquares)
print("\n")

print("Concatenate lists")
listExtended = listOfSquares + [36, 49, 64, 81, 100]
print("Result of 2 concatenated lists which is listExtended ", listExtended)
print("\n")
listOfCubes = [1, 8, 27, 65, 125]
print("list of cubes of numbers up to 5", listOfCubes)
print("\n")
print("We observed that the cube of 4 is certainly not 65. We need to correct it. So, the corrected list is ...")
listOfCubes[3] = 64
print(listOfCubes)

listOfCubes.append(6**3)
listOfCubes.append(7**3)
print("\n")
print("Extending the list of cubes ", listOfCubes)

letters = ['a', 'b', 'c', 'd', 'e']
print("list of letters -- ", letters)

print("\n")
letters[2:5] = ['C', 'D', 'E']
print("the new updated list", letters)

letters[2] = []
print("The new list after removing index 2 element is --", letters)
print("strange observation -- removing an item from the list does not change its size :( ")
print(len(letters))
