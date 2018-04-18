# Su Go,
# source: cracking the coding Interviews
# File Naming conventions are programName_problemNumber.py
# problem 1.4

def isAnagrams(string1, string2):
    '''
    Write a method to decide if two strings are anagrams or not.
    '''
    no_of_chars = 256
    if len(string1) == len(string2):
        charCount_string1 = [0]*no_of_chars
        charCount_string2 = [0]*no_of_chars
        for i in string1:
            charCount_string1[ord(i)] +=1
        for j in string2:
            charCount_string2[ord(j)] +=1
        for k in range(no_of_chars):
            if charCount_string1[k] == charCount_string2[k]:
                return 1
    else:
        return 0

# test case
string1 = "listen"
string2 = "silent"
print("Input strings are:: 1. ", string1, " 2.", string2)
print("Result of anagram test:: ", isAnagrams(string1, string2))
