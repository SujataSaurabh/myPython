#	SuGo, 20 August 2018
#	This program implements two stacks using one array
# Methodology:
#	Use one array. Start two stacks type implementation from two extreme corners 	    of the array. That is, star one stack from the left corner and second stack from the right most corner. Fill the left stack towards right and right stack moving towards left. 

# webref:https://www.geeksforgeeks.org/implement-two-stacks-in-an-array/

class twoStacks:
	def __init__(self, sizeofArray):
		self.items  = [None]*sizeofArray
		self.top1   = -1   # counter pointing to the leftmost position
		self.top2   = sizeofArray
		self.sizeofArray = sizeofArray
	def push1(self, data):
		if(self.top1<self.top2-1):
			self.top1 = self.top1 + 1
			self.items[self.top1] = data
	def push2(self, data):
		if(self.top1<self.top2-1):
			self.top2 = self.top2 - 1
			self.items[self.top2] = data
	def pop1(self):
		if(self.top1>=0):
			item = self.items[self.top1]
			self.top1 = self.top1 -1
			return item
	def pop2(self):
		if(self.top2<self.sizeofArray):
			item = self.items[self.top2]
			self.top2 = self.top2 + 1
			return item

##	*****
ts = twoStacks(4)
ts.push1(1)
ts.push1(10)
ts.push2(2)
ts.push2(20)
print(ts.pop1())
print(ts.pop2())

