class node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
class linkList(object):
  def __init__(self):
    self.head = None
  
  def add2Last(self, data):
    newNode = node(data)
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
    
  def isPalindrome(self):
    # simple solution using O(n) space and time complexity
    vals = []
    temp = self.head
    while temp:
        vals.append(temp.data)
        temp  = temp.next
    return (vals == vals[::-1])

  def isPalindrome2(self):
    '''
    *** leetcode solution *** 
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt
    # compare the first and second half nodes
    while node: # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True
    '''
    '''
    calls reverse() function which is below.
    '''
    head = self.head
    if not head or not head.next:
      return True
    slow=fast=head
    while fast.next and fast.next.next:
      slow=slow.next
      fast=fast.next.next
        
      right=slow.next
      right=self.reverse(right)
      left=head
      while right:
        if left.data!=right.data:
          return False
        left, right=left.next, right.next
      return True
    
  def reverse(self, head):
    p=head.next
    head.next=None
    while p:
      Next=p.next
      p.next=head
      head, p = p, Next
    return head
        
      
  
ll           = linkList()
ll.head      = node(1)
ll.head.next = node(2)
ll.add2Last(2)
#ll.add2Last(1)
ll.traverse()
print("\n")
#print(ll.isPalindrome())
print(ll.isPalindrome2())
