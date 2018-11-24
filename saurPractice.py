import collections

### String related problem

# Reverse String
#  "mystring"
           
#  "gnirtsym"
#   0 -> n-0
#   1 -> n-1
#   mid -> mid

def reverse(myString):
    return myString[::-1]

# valid Palindrome

#  "a"
#  "aba"
#  "aa"
#  "malayalam"
#
#   0 -> n-0
#   1 -> n-1
#   mid -> mid
def palind(myStr):
    if myStr =="":
        return False
    n = len(myStr) #2
    midVal = n//2
    for i in range(0, midVal+1):
#        if myStr[i] == myStr[n-i-1]:
#            if i == midVal:
#                return True
#            else: 
#                continue
#        else:
#            return False
        if myStr[i] != myStr[n-i-1]:
            return False
    return True       

# Skip: Comma, Spaces, Semi-colon
#  "a"
#  "aba"
#  "aa"
#  "malayalam"
#
#   0 -> n-0
#   1 -> n-1
#   mid -> mid
# ex:  "A man, a plan, a canal: Panama"
# Sol1: With extra string
# TC: O(n)
# SC: O(n)
# Sol2: Without extra string
# TC: O(n)
# SC: O(1)

def palind_skip_old(myStr):
    if myStr =="":
        return False
   # myStr = myStr.lower()
    myStr1 = ""
    for i in range(0, len(myStr)):
        if myStr[i].isalpha():
            myStr1 = myStr1 + myStr[i].lower()
    return (palind(myStr1))  
    
# # Sol2: Without extra string
# TC: O(n)
# SC: O(1)
def palind_skip(myStr):
    if myStr =="":
        return False
    start = 0
    end = len(myStr) -1
    while start < end:
        if not myStr[start].isalpha():
            start = start + 1;
        elif not myStr[end].isalpha():
            end = end - 1;
        elif not myStr[start].lower() == myStr[end].lower():
            return False
        else:
            start = start + 1;
            end = end - 1;
    return True

# valid Anagram
#
# str1, str2 => true/false 
# 
# "abc" , "bca" => true
# "abdc" , "fbca" => false
# "", "" => true
# "a", "a" => true
#
# "aa" , "a" => false
# Solution #1
# sort(str1) == sort(str2) 
# TC: O(n*log(n)) // for sorting, n is max(len(str1), len(str2))
# SC: O(1)
#
# Solution #2 (using two dictionary)
# "Same set of characters, and same frequency of each character"
#  str1 => dict1: Dictionary [character => frequence]
#  str2 => dict2: Dictionary [character => frequence]
#  result dict1 == dict2
# TC: O(n), n is max(len(str1), len(str2))
# SC: O(n)
#
#Solution #3 (using one dictionary)
# "Same set of characters, and same frequency of each character"
#  str1 => dict1: Dictionary [character => frequence]
#  str2 => dict2: Dictionary [character => frequence]
#  result dict1 == dict2
# TC: O(n), n is max(len(str1), len(str2))
# SC: O(n)

def anagram_using_counter(str1, str2):
    col1 = collections.Counter(str1)
    col2 = collections.Counter(str2)
    return col1 ==col2;

def anagram_with_two_dict(str1, str2):
    dict1 = {}
    dict2 = {}
    if len(str1)!=len(str2): return False
    for val in (str1):
        if val in dict1:
            dict1[val] = dict1[val] + 1
        else:
            dict1[val] = 1
    for val in (str2):
        if val in dict2:
            dict2[val] = dict2[val] + 1
        else:
            dict2[val] = 1
    return dict1 == dict2

def anagram(str1, str2):
    dict1 = {}
    if len(str1)!=len(str2): return False
    for val in (str1):
        if val in dict1:
            dict1[val] = dict1[val] + 1
        else:
            dict1[val] = 1
    for val in (str2):
        if val in dict1:
            if dict1[val] == 0:
                return False
            dict1[val] = dict1[val] - 1
        else:
            return False
    return True

# implement str str
# str1, str2 => idx
# "abcdef" , "bcd" => 1
# "abcdef" , "de" => 3
# "abcdef" , "bd" => -1
# "abcdef" , "fg" => -1
#
# "abcdef"
# "de"        [i=0, j=(0,2)]
#  "de"       [i=1, j=(0,2)]
#   "de"      [i=2, j=(0,2)]
#    "de"     [i=3, j=(0,2)]
#
#  "abcdef" =>len=6
#   012345
#  "defg" => 4
# 
def strStr(str1, str2):
    # assumption: str1 is the main string
    len1 = len(str1)
    len2 = len(str2)
    for i in range(0, len1 - len2 + 1):
        for j in range(0, len2):
            if str1[i+j] != str2[j]:
                break
            if j == len2 - 1:
                return i
    return -1

# string to integer

#test  cases

def test_reverse(in_, out_):
    out = reverse(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)
   
def test_palidrome(in_, out_):
    out = palind(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)

def test_palidrome_skip(in_, out_):
    out = palind_skip_old(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)
    out = palind_skip(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)


def test_anagram(in1_, in2_, out_):
    out = anagram_using_counter(in1_, in2_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)
    out = anagram_with_two_dict(in1_, in2_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)
    out = anagram(in1_, in2_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)

def test_strStr(in1_, in2_, out_):
    out = strStr(in1_, in2_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)
    
def run_tests():
    test_reverse("", "")
    test_reverse("a", "a")
    test_reverse("ab", "ba")
    test_reverse("abc", "cba")
    test_reverse("abcd", "dcba")

    test_palidrome("", False)
    test_palidrome("a", True)
    test_palidrome("aba", True)
    test_palidrome("abba", True)
    test_palidrome("abcba", True)
    test_palidrome("ab", False)
    test_palidrome("abc", False)
    test_palidrome("abcd", False)
    test_palidrome("abcde", False)

    test_palidrome_skip("", False)
    test_palidrome_skip("a", True)
    test_palidrome_skip("aA", True)
    test_palidrome_skip("A man, a plan, a canal: Panama", True)
    
    test_anagram("", "", True)
    test_anagram("a", "a", True)
    test_anagram("ab", "ab", True)
    test_anagram("ab", "ba", True)
    test_anagram("ab", "a", False)
    test_anagram("ab", "ac", False)
    test_anagram("ab", "cd", False)
    test_anagram("aab", "aba", True)
    test_anagram("aab", "ab", False)
    test_anagram("aab", "abb", False)
    test_anagram("aabb", "abb", False)
    
    test_strStr("a", "a", 0)
    test_strStr("a", "ab", -1)
    test_strStr("abcdef", "abc", 0)
    test_strStr("abcdef", "bcd", 1)
    test_strStr("abcdef", "def", 3)
    test_strStr("abcdef", "efg", -1)
    
    
run_tests();


