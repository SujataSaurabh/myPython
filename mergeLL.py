# merge two sorted LL
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/

#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together (do not create new LL, use the existing nodes) the nodes of the first two lists.

#
#  L1: [None]
#  L2: 1->2->3->None
#  O: 1->2->3->None
#
#  L1: 0->None
#  L2: 1->2->3->None
#  O: 0->1->2->-3->None
#
#  L1: 0->2->4->6->None
#  L2: 1->2->3->None
#  O: 0->1->2->2->-3->4->6->None
#
#  L1: 0->2->4->6->None
#            ^
#  L2: 1->2->3->None
#               ^
#   O: 0->1->2->2->3
#         ^
#   O: [-1]->0->1->2->2->3
#   
# newHead = O = Node(-1) // dummmy head
# if (L1.val < L2.val)
#      newHead = O = L1
#      L1 = L1.next
#  else
# .    ...
#  while L1 && L2:
#       if (L1.val < L2.val)
#             O.next = L1
#             L1 = L1.next
#       else
#          O.next = L2
#          L2 = L2.next
#       O = O.next 
#  if L2 == None:
#     O.next = L1
#  else:
#     O.next = L2
#
# 
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

class linkList(object):
  def __init__(self):
    self.head = None
    
  def add2First(self, data):
    newNode       = Node(data)
    if self.head == None:
      self.head = newNode
    else:
      newNode.next  = self.head
      self.head   = newNode
  
  def add2Last(self, data):
    newNode = Node(data)
    if self.head == None:
      self.head = newNode
    else:
      temp    = self.head
      while(temp.next):
        temp = temp.next
      temp.next    = newNode
      newNode.next = None
  
  def traverse(self):
    temp = self.head
    while (temp):
      print(temp.data, end ="->")
      temp = temp.next
  
def mergeLL(tmp1, tmp2):
    newHead = current = Node(-1)
    #tmp1 = list1 
    #tmp2 = list2 
    while(tmp1 and tmp2):
      if tmp1.data <= tmp2.data:
        current.next = tmp1
        tmp1        = tmp1.next
        current      = current.next
      else:
        current.next = tmp2
        tmp2        = tmp2.next
        current      = current.next
    if tmp1 == None:
      current.next = tmp2
    else:
      current.next = tmp1
    #newHead.next   = current
    return newHead.next

def mergeLists(list1, list2):
    """
    USING RECURSION
    Error!! uses infinite loop ...
    """
    Out = Node(-1)
    if list1 == None:
      return list2
    if list2 == None:
      return list1
    while(list1 and list2):
      if list1.data<= list2.data:
        Out = list1
        Out.next = mergeLists(list1.next, list2)
      else:
        Out = list2
        Out.next = mergeLists(list1, list2.next)      
      return Out.next   
#
n = Node(1)
ll1 = linkList()
ll2 = linkList()
print("\n LL 1...")
ll1.head      = n        # 1st node
ll1.head.next = Node(2) # 2nd node
# 3               4                 5th node
ll1.add2Last(3); ll1.add2Last(4); ll1.add2Last(5)
ll1.traverse()
print("\n LL 2...")
ll2.head      = Node(0)
ll2.head.next = Node(1)
ll2.add2Last(3)
ll2.add2Last(4)
ll2.traverse()
ll3 = linkList()
print("\n Merging 2 LLs...")
ll3.head = mergeLL(ll1.head, ll2.head)
ll3.traverse()
# 
#ll4 = linkList()
#ll4.head = mergeLists(ll1.head, ll2.head)
#ll4.traverse()

