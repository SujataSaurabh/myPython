#	SuGo, 15 August 2018
#	USe of Python sets and few of its functions

# define sets
planets = set(("Earth", "Mars", "Jupoiter"))
print(planets)

planets.add("Pluto")
print(planets)

fullList  = set(("Earth", "Mars", "Jupiter", "Mercury", "Venus", "Saturn", "Neptune", "Pluto"))
print(fullList)
print(fullList.difference(planets))
