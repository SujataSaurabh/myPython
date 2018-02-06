# This program explains the available methods that can be applied on the list data structures
# source -- https://www.dotnetperls.com/list-python
# SuGo

listInitial = []
print("length of list initially", len(listInitial))

# Append method demo
listInitial.append(1)
listInitial.append(2)
listInitial.append(6)
listInitial.append(3)
print(listInitial)
print("New length", len(listInitial))

#Insert method
lisText = ["dots", "perls"]
print(lisText)
lisText.insert(1, "net")
print("insert method used and now new list is -- ", lisText)

# Extend method  -- used to extend the list
print("Extend method ...")
a = [1,2,3]
b = [4,5,6]
print("list a and b", a, b)
a.extend(b)
print("print list a after extend it \n", a)

# Use the "in" keyword to search for an item in the list
items = ["book", "computer", "keys", "mug"]
print("\nUSE OF \"in\" METHOD TO LOOK FOR THE ITEMS IN A LIST.\n The original list is -- ", items)
print(" \n")
print("check if Computer is in the list")
if "computer" in items:
    print("yes, computer is there \n")
else:
    print("sorry, try again \n")

print("check if marker is there in the list")
if "marker" not in items:
    print("you are right, marker is not there")
