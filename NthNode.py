# Given a linked list, remove the n-th node from the end of list and return its head.
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Given n will always be valid
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

class linkList(object):
  def __init__(self):
    self.head = None
    
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
    if self.head != None:
      temp = self.head
      while (temp):
        print(temp.data, end = "->")
        temp = temp.next
    else:
      return
  def countNodes(self):
    if self.head == None:
      return 0
    else:
      count = 0
      temp = self.head
      while(temp.next):
        count +=1
        temp   = temp.next
    return count+1
  
  def nthNodefromLast(self, n):
    """
    Implementation 1
    """
    c = self.countNodes()
    ctr = 0
    nodeatPos = c-n
    temp = self.head
    while(temp):
      temp =temp.next
      ctr +=1
      if ctr == nodeatPos:
        break
    return temp.data
      
  def nthNode1pass(self, n):
    '''
    1 10 12 15 45 50
         ^
    |     
    '''
    pt1 = pt2 = self.head 
    c = 0
    while(pt1.next):
      pt1 = pt1.next
      c = c+1
      if c==(n-1):
        break
    while pt1.next:
      prev = pt2
      pt2  = pt2.next
      pt1  = pt1.next
    return pt2.data
  
  def removeNthfromLast(self, n):
    dummy = Node(-1)
    dummy.next = self.head
    self.head = dummy
    pt1 = pt2 = self.head 
    c = 1
    while(pt1.next):
      pt1 = pt1.next
      c = c+1
      if c==(n):
        print("c " , c)
        break
    while pt1.next: 
        prev = pt2
        pt2  = pt2.next
        pt1  = pt1.next
    prev.next = pt2.next
    del pt2
 #   return dummy.next
  
  def removeNth(self, n):
    dummy = Node(-1)
    dummy.next = self.head
    self.head = dummy
    c = self.countNodes()
    ctr = 0
    nodeatPos = c-n
    temp = self.head
    while(temp):
      prev = temp 
      temp = temp.next
      ctr +=1
      if ctr == nodeatPos:
        break
    prev.next = temp.next
    del temp
    return dummy.next  
# ***  LINKLIST ***    
ll = linkList()
ll.head = Node(1)
ll.head.next = Node(10)
ll.add2Last(12)
ll.add2Last(15)
ll.add2Last(45)
ll.add2Last(50)
ll.traverse()
print("\n Nth node ...(1) using count and (2) using single pass")
print(ll.nthNodefromLast(2))
print(ll.nthNode1pass(2))

print("\n Nth node from last ...")
ll.removeNth(2)
ll.traverse()

print("\n special case ...")
ll2 = linkList()
ll2.head = Node(1)
ll2.head.next = None
ll2.traverse()
print("\n removing the single node")
print(ll2.removeNth(1))
