# This program has been taken from the website:
# https://learnpythonthehardway.org/python3/ex5.html

myName      = 'Sujata'
myAge       = 35    #years
myHeight    = 60    #inches
myWeight    = 53    # kgs
myEyes      = 'brown'
myTeeth     = 'white'
myHair      = 'brown'

print(f"Let's talk about {myName}")
print(f"She is {myHeight} inches tall")
print(f"She is {myWeight} heavy")
print("Actually that's underweight")
print(f"She's got {myEyes} eyes and {myHair} hair")
print(f"Her teeth are actually {myTeeth} depending upon how often she brushes")
# be careful!
total = myAge + myHeight + myWeight
print(f"If I add {myAge}, {myHeight} and {myWeight}, I get {total}")
