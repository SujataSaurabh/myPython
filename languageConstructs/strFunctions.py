#	SuGo, 14 August 2018
#	List and demonstration of string functiions

print("  DEMO:: startswith(), endwith() and in operator \n ")
str1 = input("Enter a continuous string:: ")
print("Entered string (str1)  is ", str1), "\n"

startSearch = input("Enter the string to search if your entered stringstarts with the same  ")
print(str1.startswith(startSearch), "\n")

endSearch = input("Enter string to search if your entered string ends with the same  ")
print(str1.endswith(endSearch), "\n")

inSearch = input("Enter the substring to check whether it is a part of the main string or not  ")
print(inSearch in str1, "\n")

#print("str1.startswith('Rhino') \n")
#print(str1.startswith("Rhino"))
#print("str1.endswith('tamus') \n")
#print(str1.endswith("tamus"))
#print("'pot' in str1")
#print("pot" in str1)
#print("'lamb' in str1")
#print("lamb" in str1)
