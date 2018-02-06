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
