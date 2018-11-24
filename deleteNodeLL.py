class ListNode(object):
    def __init__(self, x):
          self.val  = x
          self.next = None

class Solution(object):
    def __init__(self):
      self.head  = None
     # self.next = None
      
    def deleteNode(self, nodeVal):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if self.head == None:
          return
        else:
          temp = self.head
          while(temp.val != nodeVal):
            print("temp val ", temp.val)
            prev = temp
            temp = temp.next
          prev.next = temp.next
          del temp
          
    def addNode(self, node):
        newNode = ListNode(node)
        if self.head == None:
          self = newNode
        else:
          temp = self.head
          while temp.next:
            temp = temp.next
          temp.next = newNode
    def traverse(self):
        temp  = self.head
        while(temp):
          print(temp.val)
          temp = temp.next
        
ln1         = ListNode(4)
ln2         = ListNode(5)
s           = Solution()
s.head      = ln1
s.head.next = ln2
s.addNode(5)
s.addNode(1)
s.addNode(9)
s.traverse()
print("deleting node")
s.deleteNode(5)
s.traverse()
