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
  
  def traverse(self):
    temp = self.head
    while (temp):
      print(temp.data, end = "->")
      temp = temp.next
      
  def isCycle(self):
    fast = slow = self.head
    while fast and slow:
      try:
        fast = fast.next.next
        slow = slow.next
      except:
        return False
      if fast == slow:
        return True
    return False
    
  def hasCycle(self):
    """method 2"""
    #Method 2:
    dummy = Node(-1)
    while self.head:
      if self.head == dummy: return True
      temp = self.head
      self.head = self.head.next
      temp.next = dummy
    return False
    
ll = linkList()
ll.head = Node(2)
ll.head.next = Node(2)
#ll.add2First(3)
#ll.add2First(1)
ll.traverse()
print("\n isCycle")
print(ll.hasCycle())
