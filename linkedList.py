# This program implements an unordered linked list
# ref:http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html#the-node-class

#implement a class called 'node'

class node:
    def __init__(self, initVal):
        self.data = initVal
        self.next = None

    def getVal(self):
        return self.data

    def setVal(self, newVal):
        self.data = newVal

    def getNext(self):
         return self.next

    def setNext(self, newNext):
        self.next = newNext  # class and its function definition ends here

class unorderedList:
    def __init__(self):
        self.head = None
        size = 0
    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = node(item)
        temp.setNext(self.head)
        self.head = temp
    #    size+=1
        return True
        ## linkedlist traversal functions --search, size and remove
    def size(self):
        current = self.head
        count = 0
        while current!= None:
            count =  count+1
            current = current.getNext()

        return count

    def printList(self):
        current = self.head
    #    print(current.getVal())
        while current!= None:
            print(current.getVal())
            current = current.getNext()

    def search(self, item):
        current = self.head
        itemFound = False
        while current!=None and not itemFound:
            if current.getVal() == item:
                itemFound = True
            else:
                current  = current.getNext()
        return itemFound

    def remove(self, item):
        current = self.head
        previous = None
        itemFound = False
        while not itemFound:
            if current.getVal()==item:
                itemFound = True
            else:
                previous = current
                current = current.getNext()

        previous.setNext(current.getNext())

    def append(self, item):
        temp = node(item)
        temp.setNext(None)
        current = self.head
        if current:
            while current.getNext()!=None:
                current = current.getNext()
            current.setNext(temp)
        else:
            self.head = Node(item)
# now use the class functions
    myList  = unorderedList()
    print(myList.add(10))
    print(myList.add(11))
    print(myList.add(12))
    print(myList.add(22))

    size_ll = myList.size()
    print("Number of items in Linked list are: \t" + str(size_ll))
    print("The items in the linked list are: ")
    myList.printList()
    print(myList.search(22))
    myList.remove(10)
    print("New linked list is: ")
    myList.printList()
    myList.append(23)
    print("appending 23")
    myList.printList()
# define an object of class node with name 'temp' and value '93'
# temp =  node(93)
# print its value
# print(temp.getVal())
# set next node value
# temp.setNext(10)
# temp.setNext(11)
# print it
# print(temp.getNext())
# print(temp.getVal())
