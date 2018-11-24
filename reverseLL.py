class Node:
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
    temp = self.head
    while (temp):
      print(temp.data, end = "->")
      temp = temp.next

  def reverseLL(self):
    '''
      1 -> 2 -> 5 -> 6 ->8 -> None
      1<-  2<-  5<-  6<- 8     
    '''
    current = self.head
    prev    = None
    next_   = None
    while(current):
      next_        = current.next
      current.next = prev
      prev         = current
      current      = next_
    self.head = prev
                
  def recursiveReverse(self):
    '''
    To do correct implementation 
    '''
    node = self.head
    self.recRev(self, node)
  
  def recRev(self, node, prev =None):
    if not  node:
      return prev
    recurseN  = node.next
    node.next = prev
    return self.recRev(recurseN, node)
     
      

ll = linkList()
first = Node(1)
sec   = Node(2)
ll.head = first 
ll.head.next = sec

ll.add2Last(5)
ll.add2Last(6)
ll.add2Last(8)
print("\n linked List...")
ll.traverse()

print("\n \n Reverse linked list...")
ll.reverseLL()
ll.traverse()

print("\n \n Reverse 2")
#ll.recursiveReverse()
#ll.traverse()
