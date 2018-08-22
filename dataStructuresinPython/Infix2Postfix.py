#	SuGo, 22 August 2018
#	Implement infix to postfix conversion of an expression using Stack
# 	Algorithm --
#	1. Scan infix expression from left to right
#	2. If operand then put that in the postfix array/list
#	3. If operator then:
#		(a) If stack empty then push the current scanned operator into it
#		(b) If stack not empty then
#			check the precedence of the two operators -- 1. on the top of the stack [T]  and 2. current operator in the scanned Infix expression [C]
#			If precedence of [T] > precedence of [C] then:
#				push [C] operator on the top of the stack 
#			else:
#				pop [T] operator from the stack and apend it to the postfix array
#
#	webref: https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/

class Conversion:
	
	def __init__(self, exprLength):
		self.top 	= -1
		self.exprLen 	= exprLength
		
		self.stack	= []
		
		self.postfix	= []
		self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

	def isEmpty(self):
		return True if self.top == -1 else False
		
	def topofStack(self):
		return self.stack[-1]   # -1 is the top of the stack

	def pop(self):
		if self.isEmpty():
			return "$"
		else:
			self.top = self.top - 1
			return self.stack.pop()
	
	def push(self, item):
		self.stack.append(item)
		self.top = self.top + 1

	def isOperand(self, item):
		'''To distinguish between the scanned operand and operator '''
		return item.isalpha()

	def comparePrecedence(self, operator):
		# get the precedences of two operators 
		# 1. input 'operator' and 2. 'top' of stack
		precOp1 = self.precedence[operator]
		precOp2 = self.precedence[self.topofStack()]
		
		return True if precOp1 <= precOp2 else False
	
	def infix2postfix (self, InExpr):
		lenInExpr = len (InExpr) 
		for i in InExpr:
			if Conversion.isOperand (self, i):
				self.postfix.append (i)
			else:
				#it is operator. now check precedences
				if Conversion.isEmpty (self):
					self.push (i)
				else:
				    while (not self.isEmpty() and Conversion.comparePrecedence (self, i)):
				        self.postfix.append(self.pop())
				    self.push(i)
		while not self.isEmpty():
		    self.postfix.append(self.pop())
		print("".join(self.postfix))
		
#
ex = "a+b*d^e+r" 
con = Conversion(len(ex)) 
con.infix2postfix(ex)

		
