#	SuGo, 2 Sep 2018
#	Implementation of Counter datatypes inbuilt in python
#
import collections
#	Initialization
print(collections.Counter(["a", "b", "b", "c", "a"]))
print(collections.Counter({"a":2, "b":2, "c":1}))
print(collections.Counter(a = 2, b = 2, c =1))

#	update method in Counter
c = collections.Counter()
print("1st c ", c)
c.update('abcdaab')
print("2nd c ", c)
c.update({"d":3, "e":1})
print("3rd c", c)


# Counter keep the count of the elements 
c = collections.Counter("abcdefdef")
for letter in "abcde":
	print("letter ", letter, " comes ",   c[letter], " any times!")
