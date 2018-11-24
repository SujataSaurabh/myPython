# good solutions page
#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34680/Python:-Recursion-version-and-Iteration-version-easy-to-understand
import collections
import queue
# Binary Tree

class Tree:
    def __init__(self, val, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(node):
    return
    
def count_nodes(node):
    if node == None:
        return 0
    c = 1
    cleft  = c + count_nodes(node.left) 
    cright = c + count_nodes(node.right)
    return (cleft+cright-1)

def sum_nodes(node):
    if node== None:
        return 0
    s = node.val
    return s + sum_nodes(node.left) + sum_nodes(node.right)

def max_val(node):
    if node == None:
        return 0
    maxVal       = node.val
    maxLeft      = max_val(node.left)
    maxRight     = max_val(node.right)
    return max(maxVal, maxLeft, maxRight)

def searchTree(node, searchVal):
    if node == None:
        return False
    if node.val == searchVal:
        return True
    return searchTree(node.left, searchVal) or searchTree(node.right, searchVal)

'''
                      1(0)
              2(1)......|........3(2)
          4(3).|.5(4)       6(5).|.7(6)

BFS result: 1, 2, 3, 4, 5, 6, 7
p = [1]
c = []


q1

q2

Level Order Traversal:
1
2 3
4 5 6 7


'''
def bfs(node):
    if node == None:
        return None
    que = queue.Queue(maxsize=20)    
    que.put(node)
    while not que.empty():
        node = que.get()
        print(node.val)
        if node.left!= None:
            que.put(node.left)
        if node.right!= None:
            que.put(node.right)
#
# print every level in a new row
def bfs_level(node):
    if node == None:
        return None
    parent = queue.Queue(maxsize=20) 
    child  = queue.Queue(maxsize=20) 
    parent.put(node)
    while not parent.empty() or not child.empty():
        if not parent.empty():
            node = parent.get()
            print(node.val)
            if node.left!= None:
                child.put(node.left)
            if node.right!= None:
                child.put(node.right)
        else:
             parent, child = child, parent
             print("next line \n")
             

def inorder(node):
    if node== None:
        return None
    inorder(node.left)
    print(node.val)
    inorder(node.right)
            
#test  cases 
def test_count_nodes(in_, out_):
    out = count_nodes(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)

def test_sum_nodes(in_, out_):
    out = sum_nodes(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)

def test_max_val(in_, out_):
    out = max_val(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)

def test_search(in1_, in2_, out_):
    out = searchTree(in1_, in2_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)
    
def test_bfs(in_, out_):
    out = bfs(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)   

def test_bfs_level(in_, out_):
    out = bfs_level(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)   


def array_to_tree(arr):       
    if not arr: 
        return None
    mid        = (len(arr)) // 2
    root       = Tree(arr[mid]) 
    root.left  = array_to_tree(arr[:mid]) 
    root.right = array_to_tree(arr[mid+1:]) 
    return root 

#            3
#       2    |     5
#      1|None     4|None
#
#
#
def array_to_tree_with_print(arr):       
    if not arr: 
        return None
    mid        = (len(arr)) // 2
    root       = Tree(arr[mid]) 
    root.left  = array_to_tree_with_print(arr[:mid]) 
    root.right = array_to_tree_with_print(arr[mid+1:]) 
    print(str(root.val) + ", => left: " + str ( root.left.val if root.left else None) + ", => right: " + str (root.right.val if root.right else None))
    return root 


def run_tests():
    test_count_nodes(array_to_tree([]), 0)
    test_count_nodes(array_to_tree([1]), 1)
    test_count_nodes(array_to_tree([1, 2, 3]), 3)

    test_sum_nodes(array_to_tree([]), 0)
    test_sum_nodes(array_to_tree([1]), 1)
    test_sum_nodes(array_to_tree([1, 2, 3]), 6)

    test_max_val(array_to_tree([]), 0)
    test_max_val(array_to_tree([1]), 1)
    test_max_val(array_to_tree([1, 2, 3, 4]), 4)
    test_max_val(array_to_tree([4, 3, 2, 1]), 4)
    test_max_val(array_to_tree([1, 2, 3, 4, 3]), 4)
    test_max_val(array_to_tree([1, 2, 3, 4, 3, 2, 1, 3]), 4)

    test_search(array_to_tree([]), 0, False)
    test_search(array_to_tree([]), 1, False)
    test_search(array_to_tree([1]), 0, False)
    test_search(array_to_tree([1]), 1, True)
    test_search(array_to_tree([1, 2, 3]), 1, True)
    test_search(array_to_tree([1, 2, 3]), 2, True)
    test_search(array_to_tree([1, 2, 3]), 6, False)
    test_search(array_to_tree([1, 2, 3, 4]), 1, True)
    test_search(array_to_tree([1, 2, 3, 4]), 2, True)
    test_search(array_to_tree([1, 2, 3, 4]), 4, True)
    test_search(array_to_tree([1, 2, 3, 4]), 0, False)
    test_search(array_to_tree([1, 2, 3, 4]), 6, False)

#    test_bfs(array_to_tree([]), None)
#    test_bfs(array_to_tree([1]), None)
#    test_bfs(array_to_tree([1, 2, 3]), None)
#    test_bfs(array_to_tree([1, 2, 3, 4, 5]), None)
#    test_bfs(array_to_tree([1, 2, 3, 4, 5]), None)

    test_bfs_level(array_to_tree([1, 2, 3, 4, 5]), None)
    
           
run_tests();
