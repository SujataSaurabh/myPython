import collections
# Recursion + Tree
class List:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def sum_one_to_n(n):
    if n ==0:
        return 0
    return n+ sum_one_to_n(n-1)

def print_list(list1):
    result = ""
    while list1:
        result += "->" +  str(list1.val)
        list1 = list1.next
    return result

def compare(list1, list2): 
    if list1 == None:
        return list2 == None
    while list2:
        if not list1:
            return False
        if not list2.val == list1.val:
            return False
        list1 =list1.next
        list2 = list2.next
    return list1 == None
    
# Recursive program example    
def multiply_one_to_n(n):
    '''
    Given an integer n, will return multiplication of 1..2..3..4.....n-1..n
    '''
    if n < 1:
        raise Exception('Invalid input, n should be greater than or equal to 1')
    if n == 1:
        return 1
    return n * multiply_one_to_n(n-1)

def count_nodes(list):
    if list == None:
        return 0
    c = 1 
    return c + count_nodes(list.next)

def sum_nodes(list):
    if list==None:
        return 0
    s = list.val
    return s + sum_nodes(list.next)

def max_val(list):
    if list ==None:
        return 0
    maxVal = list.val
    n      = max_val(list.next)
    return max(maxVal, n)

# None    ->    1  ->   2     -> 3   -> 4    -> None
#   p           c         
#
# None          1  ->   2     -> 3   -> 4    -> None
#   p           c       tmp
#
# None    <-    1       2     -> 3   -> 4    -> None
#   p           c       tmp  
#
# None    <-    1       2     -> 3   -> 4    -> None
#   p           c       tmp  
#
# None    <-    1       2     -> 3   -> 4    -> None)
#              p,c      tmp  
#
# None    <-    1       2    ->  3   -> 4    -> None  [1st loop ends here]
#               p       c
#
#                        
# curr.next = prev
# curr      = next
# 
# 1<-2<-3<-4
# 
def reverse1(Llist):
    if Llist == None:
        return None
    p = None
    c = Llist
    while c:
        tmp    = c.next
        c.next = p
        p      = c
        c      = tmp
    return p

# 1 -> 2 -> 3 -> 4
# 1,  None <- 2 <-3 <- 4
# None <-1 <- 2 <-3 <- 4
# recursive method
def reverse(node):
    if node == None or node.next == None:
        return node
    cur      = node
    nextNode = node.next
    print("Before reverse: ", cur.val)
    result        = reverse(node.next)
    nextNode.next = cur    
    cur.next      = None
    print("After reverse: ", cur.val)
    print("result: ", print_list(result))
    return result
    
# test  cases
def test_sum_one_to_n(in_, out_):
    out = sum_one_to_n(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)

def test_multiply_one_to_n(in_, out_):
    out = multiply_one_to_n(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)
   
def test_count_nodes(in_, out_):
    out = count_nodes(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)

def test_sum_nodes(in_, out_):
    out = sum_nodes(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)

def test_max_val(in_, out_):
    out = max_val(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)

def test_reverse(in_, out_):
    out = reverse(in_)
    assert compare(out_, out), "Expected " + str(out_) + ", found: " + str(out)

def array_to_list(arr):
    head = l = List(0)
    for i in range(len(arr)):
        node = List(arr[i])
        l.next = node
        l = l.next
    return head.next

def run_tests():

    test_sum_one_to_n(1, 1)
    test_sum_one_to_n(4, 10)

    test_multiply_one_to_n(1, 1)
    test_multiply_one_to_n(4, 24)
    
    test_count_nodes(array_to_list([]), 0)
    test_count_nodes(array_to_list([1]), 1)
    test_count_nodes(array_to_list([1, 2, 3]), 3)

    test_sum_nodes(array_to_list([]), 0)
    test_sum_nodes(array_to_list([1]), 1)
    test_sum_nodes(array_to_list([1, 2, 3]), 6)

    test_max_val(array_to_list([]), 0)
    test_max_val(array_to_list([1]), 1)
    test_max_val(array_to_list([1, 2, 3, 4]), 4)
    test_max_val(array_to_list([4, 3, 2, 1]), 4)
    test_max_val(array_to_list([1, 2, 3, 4, 3]), 4)
    test_max_val(array_to_list([1, 2, 3, 4, 3, 2, 1, 3]), 4)

#    test_reverse(array_to_list([]), array_to_list([]))
#    test_reverse(array_to_list([1]), array_to_list([1]))
#    test_reverse(array_to_list([1, 2]), array_to_list([2, 1]))
#    test_reverse(array_to_list([1, 2, 3]), array_to_list([3, 2, 1]))
    test_reverse(array_to_list([1, 2, 3, 4]), array_to_list([4, 3, 2, 1]))
        
run_tests();
