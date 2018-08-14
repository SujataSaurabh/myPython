#	SuG0, 14 August 2018
#	This program finds the number of vowels and consonants present in a string
#	webref: https://www.ict.social/python/basics/strings-in-python-working-with-single-characters

Str_Main = "a programmer gets stuck in the shower because the instructions on the shampoo were: Lather, wash and repeat."
# convert the entire sting to the lower letters
Str_2	= Str_Main.lower()

# define the string of vowels and consonants
vowel = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

# counter set
vowelCount     = 0
consonantCount = 0

for char in Str_2:
	if char in vowel:
		vowelCount +=1
	elif char in consonants:
		consonantCount +=1

print("Vowels ", vowelCount)
print("\n Consonants  ", consonantCount)
