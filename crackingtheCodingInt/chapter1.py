# this file contains the solutions of chapter 1 of Cracking the coding Interviews
# Su Go
# Question 1.1
def unique(str1):
    '''
    Implement an algorithm to determine if a string has all unique characters. What if
    you can not use additional data structures?
    '''
    length      = len(str1)
    no_of_chars = 256
    count1      = [0]*256
    for i in str1:
        count1[ord(i)] +=1
    for j in range(no_of_chars):
        if count1[ord(i)]>1:
            return 0
    return 1

# Question 1.2
def reverseString(str1):
    '''
    Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
    five characters, including the null character.)
    '''
    return str1[::-1]

# Question 1.3
def removeDuplicates(str1):
    '''
    Design an algorithm and write code to remove
    the duplicate characters in a string without using any additional buffer.
    NOTE: One or two additional variables are fine.
    An extra copy of the array is not.
    FOLLOW UP
    Write the test cases for this method
    '''
    '''
    Method 1: using an additional buffer
    '''
    result = []
    for i in str1:
        if i not in result:
            result.append(i)
    result = ''.join(result)
    return result
# Question 1.4
def areAnagrams(str1, str2):
    '''
    Write a method to decide if two strings are anagrams or not
    '''
    no_of_chars = 256
    count1      = [0]*256
    count2      = [0]*256
    if len(str1) == len(str2):
        for i in str1:
            count1[ord(i)] += 1
        for j in str2:
            count2[ord(j)] += 1
        for k in range(no_of_chars):
            if count1[k]   == count2[k]:
                return 1
    else:
        return 0

# Question 1.5
def replaceString(str1):
    '''
    Write a method to replace all spaces in a string with ‘%20’
    '''
    print("replace string-- to be done")

# Question 1.6
def rotImage90(imageMatrix):
    '''
    Given an image represented by an NxN matrix, where each pixel in the image is 4
    bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
    '''
    length = len(imageMatrix)-1
    if len(imageMatrix) == 0:
        return imageMatrix
    else:
        for i in range(0, int(length/2)):
            for j in range(0, length-i):
                temp                            = imageMatrix[i][j]
                imageMatrix[i][j]               = imageMatrix[length-j][i]
                imageMatrix[length-j][i]        = imageMatrix[length-i][length-j]
                imageMatrix[length-i][length-j] = imageMatrix[j][length-i]
                imageMatrix[j][length-i]        = temp
        return imageMatrix

# Question 1.7
def placeRowColZero(Matrix):
    '''
    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
    column is set to 0.
    '''
    no_of_rows = len(Matrix)    # number of rows
    no_of_cols = len(Matrix[0]) # number of columns
    rowSet = set()
    colSet = set()
    if len(Matrix)>=1:
        for i in range(no_of_rows):
            for j in range(no_of_cols):
                if Matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
        for i in range(no_of_rows):
            for j in range(no_of_cols):
                if i in rowSet or j in colSet:
                    Matrix[i][j] = 0
        return Matrix

# Question 1.8
def rotationString(str1, str2):
    '''
    Assume you have a method isSubstring which checks if one word is a substring of another.
    Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
    only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).
    '''
    return str1 in str2+str2

## TEST cases
print(" *** Problem 1.1 ***")
print("is the word 'listen' unique :: ", unique("listen"))
print("is the word 'tata' unique :: ", unique("tata"), "\n")

print(" *** Problem 1.2 *** ")
print("reverse of 'sumo' :: ", reverseString("sumo"), "\n")

print(" *** Problem 1.3 *** ")
print("remove duplicates :: 'apple'", removeDuplicates("apple"))
print("remove duplicates :: 'Kiro'", removeDuplicates("Kiro"), "\n")

print(" *** Problem 1.4 *** ")
print("Test on two anagram strings:: 'listen' and 'silent' -- ", areAnagrams("listen", "silent"))
print("Are strings 'list' and 'stole' anagrams:: ", areAnagrams("list", "stole"), "\n")

print(" *** Problem 1.5 ***")
print("HAS TO BE IMPLEMENTED")

print(" *** Problem 1.6 ***")
imageMatrix = [[1, 2, 3, 5], [4, 5, 2, 1], [6, 8, 9, 0], [2, 4, 6, 1]]
print("Input matrix M :: ", imageMatrix)
print("NXN Matrix rotated 90° :: ", rotImage90(imageMatrix))
