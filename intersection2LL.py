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
  
def intersectionNode(list1, list2):
  count1 = linkList.countNodes(list1)
  count2 = linkList.countNodes(list2)
  list1 = list1.head
  list2 = list2.head
  if count1-count2>0:
    while list1:
      if list1.data == list2.data:
        print("I am ")
        return list2.data
      else:
        list1 = list1.next
        list2 = list2.next
  else:
    while list2:
      if list2.data == list1.data:
        print("here")
        return list2.data
      else:
        list1 = list1.next
        list2 = list2.next
        
def getIntersectionNode(headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # if headA or headB is None, return None
        if not headA or not headB:
            return None

        a, b = headA.head, headB.head
        # if a or b arrive the end, switch other head else move to nextself.
        # if have intersection a = b, loop break, return a or b is the intersection.
        # if no intersection they will end in None at the same time, loop break, because
        #  a, b move the same distance(a + b = b + a).  a, b are now both None. return a or b.
        while a  != b :
            a = a.next if a else headB
            b = b.next if b else headA

        return a
      
n = Node(12)
ll = linkList()
ll2 = linkList()
first = Node(10)
sec   = Node(2)
ll.head = first 
ll.head.next = sec
ll.add2First(3)
ll.add2First(5)

ll2.head = Node(4)
ll2.head.next = Node(10)
ll2.add2First(30)
ll2.add2First(7)
print(intersectionNode(ll, ll2))
