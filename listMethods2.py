# list methods to sort the items in a list
# source -- https://www.dotnetperls.com/list-python

print("There are inbuilt methods to sort and reverse a list in python, example, list.sort(), list.reverse()\n")

list = [400, 500, 100, 2000] # definition of the list
print("The original list is ...", list)

list.reverse() # standard reverse function which reverses the list
print("\n list.reverse() gives", list)
list.sort() # standards ascending sorting
print("\n list.sort() gives", list)

# Below we demostrate the use of "key" in the sort method
# It is useful to sort the key in a desired way as expplained below
print("variations of the sort method using key ...")

values = ["abc", "bca", "cab"]
print("A given list to be sorted", values)
# function defined to sort the list accoring to the characters at a specific position
def sortChar(s):
    return s[2] # we define 3rd place

values.sort(key = sortChar) # sort list with the sorted characters at the 3rd place
print("list sorted with 3rd key in the strings ...", values)

# remove or delete items from the list
names = ["Tommy", "Bill", "Janet", "Bill", "Stacy"]
print("\nthe list of names contain", names)

# remove the "Bill"
names.remove("Bill") # remove method will remove the first matching element of the list
print("new list after applying remove method ...",names)
print("observe that one \"Bill\" is omitted but another is still there in the list")

del names[2] # del can be used to remove a range of elements OR an element at a specific index location
print("\nremoving the element using \"del\" method", names)

# FOR method applied on the list
names = ["Tommy", "Bill", "Janet", "Bill", "Stacy"]

print("\n USING i ON THE LIST TO PICK UP ITS ITEMS")
for i in range(len(names)):
    print(names[i])

# OR
print("\n USING element ON THE LIST TO PICK UP ITS ITEMS")
for element in names:
    print(element)
