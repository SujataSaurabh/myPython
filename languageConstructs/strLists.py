#	SuGo, 14 August 2018
# This program demonstrates the use of strings in lists

simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]

print("\n", simpsons, "\n")
print("\n test 1 \n")
for i, item in enumerate(simpsons):
	print(i, item)

print("\n test 2 \n")

for i in enumerate(simpsons):
	print(i)

print("\n test 3 \n")

for i in simpsons:
	print(i)
