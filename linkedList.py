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
        self.next =   newNext  # class and its function definition ends here

# define an object of class node with name 'temp' and value '93'
temp =  node(93)
# print its value
print(temp.getVal())
# set next node value
temp.setNext(10)
# print it 
print(temp.getNext())
print(temp.getVal())
