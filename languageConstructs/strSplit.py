#	SuGo, 15 August 2018
#	Demo of string split() method and joi() method
# 	----   MORSE CODE DECODER    ----

#	****************************
def morseDecoder(msg):
	# declare the required variables 
	decodedMsg = ""

	alphabetChars = "abcdefghijklmnopqrstuvwxyz"
	morseChars    = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

	for char in msg:
		if char in morseChars:
			ind 	 = morseChars.index(char)
			alphabet = alphabetChars[ind]
		decodedMsg += alphabet
	return decodedMsg
		
#	**************************
# The original message
string2decode = ".. -.-. - ... --- -.-. .. .- .-.."

# split string into the Morse characters
morseChar = string2decode.split(" ")

print("Original message  ", string2decode)
print("after split message becomes ", morseChar)
print("decoded message is \n", morseDecoder(morseChar))
