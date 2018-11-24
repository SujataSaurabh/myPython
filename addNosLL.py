class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

class linkList(object):
  def __init__(self):
    self.head = None
    
  def add2First(self, data):
    newNode       = Node(data)
    if self.head  == None:
      self.head   = newNode
    else:
      newNode.next  = self.head
      self.head     = newNode
      
  def traverse(self):
    temp = self.head
    while (temp):
      print(temp.data, end = "->")
      temp = temp.next
      
  def addNos(self, list1, list2):
    carry = 0 
    root = n = Node(0)
    tmp1 = list1.head
    tmp2 = list2.head
    while tmp1 or tmp2 or carry:
      val1 = val2 = 0
      if tmp1:
        val1  = tmp1.data
        tmp1 = tmp1.next
      if tmp2:
        val2  = tmp2.data
        tmp2 = tmp2.next
      carry, val = divmod(val1+val2+carry, 10)
      n.next = Node(val)
      n = n.next
    return n.next
      
ll1 = linkList()
ll1.head     = Node(1)
ll1.head.next = Node(3)
ll1.add2First(4)

ll2 = linkList()
ll2.head     = Node(3)
ll2.head.next = Node(2)
ll2.add2First(0)
l = linkList()
print(l.addNos(ll1, ll2))
