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
  
  def addatPos(self, data, dataPos):
    newNode = Node(data)
    temp    = self.head
    while(temp.data != dataPos):
      temp = temp.next
    if temp.data!= dataPos:
      return 
    else:
      newNode.next = temp.next
      temp.next    = newNode

  def traverse(self):
    temp = self.head
    while (temp):
      print(temp.data, end = "->")
      temp = temp.next
      
  def deleteFirst(self):
    if self.head == None:
      print("nothing to be deleted")
      return 
    else:
      temp       = self.head
      del self.head
      self.head  = temp.next
  
  def deleteLast(self):
    if self.head == None:
      print("nothng to be deleted")
    else:
      temp = self.head
      while(temp.next):
        prev = temp
        temp = temp.next
      prev.next = None
      del temp
#=========================================
#  A -> B -> C -> D -> E -> F -> G -> H
#            ^   
# node.val = node.next.val;
#  A -> B -> D -> D -> E -> F -> G -> H
#            ^    t
# temp = node.next
# node.next = temp.next
# del temp
#========================================
  def delbyVal(self, dataPos):
    if self.head == None:
      print("node does not exist")
      return
    else:
      temp = self.head
      while(temp.data!=dataPos):
        prev = temp
        temp = temp.next
      prev.next = temp.next
      del temp
  
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

  def delNthNode(self, nodePos):
    if self.head == None:
      return
    else:
      c = self.countNodes()
      print("counting of nodes ...", c)
      if c<nodePos:
        print("No node exist at this position")
      else:
        temp = self.head
        prev = None
        for i in range(1, c-1):
          if i == nodePos:
            prev.next = temp.next
            del temp
          else:
            prev = temp
            temp = temp.next 
            #count_+=1

  # delNthFromLast
  #A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> K 
  #                                        ^              ^          
  #def nthNodefromLast(self, posfromLast):
  #  c = self.countNodes()
  #  temp = None
  #  count_ = 0
  #  while(temp):
  #    prev = temp
  #   temp = temp.next
  # reached last node
  # while(temp):
  #   count_ +=1
      
  def swapNodes(self, node1, node2):
    tmp = node1
    node1 = node2
    node2 = tmp
   # node2.next = node1.next
    
#     ***  Test code ***
n = Node(12)
ll = linkList()
first = Node(1)
sec   = Node(2)
ll.head = first 
ll.head.next = sec
ll.add2First(3)
ll.add2Last(5)
ll.add2Last(6)
ll.add2Last(8)
ll.addatPos(4, 2)
print("\n Full linked list ...")
ll.traverse()
print("\n deleting first ...")
ll.deleteFirst()
ll.traverse()
print("\n delete Last ...")
ll.deleteLast()
ll.traverse()
print("\n delete a Node ...")
ll.delbyVal(5)
ll.traverse()
print("\n Count of nodes ...", ll.countNodes())
print("\n swap nodes ...")
ll.swapNodes(2, 4)
ll.traverse()

      
    
    
