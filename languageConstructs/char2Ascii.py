#	SuGo, 14 August 2018
#	Converts the character/string to its ASCII code

#	--------
def char2ASCII(str1):
	Ascii = []
	for char in str1:
		Ascii.append(ord(char))
	return Ascii
#	--------
def ASCII2char(ascCode):
	charArr = []
	for i in ascCode:
		asc_char = chr(i)	
		charArr.append(asc_char)
	strFull = "".join(charArr)
	return strFull

str1 = "abcdz"
print(char2ASCII(str1))
print(ASCII2char(char2ASCII(str1)))
