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
  def oddEvenList(self):
    temp = self.head
    llEven =  linkList()
    llOdd  =  linkList()
    while temp:
      if temp.data%2 == 0:
        llEven.add2First(temp.data)
      else:
        llOdd.add2First(temp.data) 
      temp = temp.next
    tmp = llOdd.head 
    while(tmp.next):
      tmp  = tmp.next
    tmp.next = llEven.head 
    return llOdd

  def traverse(self):
    temp = self.head
    while (temp):
      print(temp.data, end = "->")
      temp = temp.next
    
ll  = linkList()
ll.head      = Node(3)
ll.head.next = Node(1)
ll.add2First(4)
ll.oddEvenList().traverse()
