# STACKS

def reversalStack(stk):
  '''
  The order that they’re removed is exactly the reverse of the order     that they were placed. This ability to reverse the order of items       is what makes stacks so important.
  '''
  result = []
  while stk:
    result.append(stk.pop())
  return result

class stack(object):
  def __init__(self):
    self.items = []
  #
  def push(self, item):
    self.items.append(item)
  #
  def pop(self):
    if self.items == []:
      return 
    else:
      self.items.pop()
  #
  def peek(self):
    return self.items[-1]
  #
  def size(self):
    return len(self.items)
  #
  def printstk(self):
    result = []
    while self.items:
      result.append(self.items.pop())
    return result
  #
def validParenthesis(stk):
  stack = []
  paren = '('
  for par in stk:
    if par == paren:
      stack.append(par)
    else:
      try:
        stk.pop()
      except IndexError:
        return False
  return len(stack)==0
  #
def validParenthesis2(stk):
  stack = []
  paren = {'(':')', '{':'}', '[':']'}
  for par in stk:
    if par in paren:
      stack.append(stk)
   #   continue
    else:
      if not stack or paren[stack.pop()]!= par:
        return False
     # try:
     #   expected_symbol = stack.pop()
     # except IndexError:
     #   return False
     # if par != paren[expected_symbol]:
     #   return False
  return not stack
 
def toBinary(decNo):
  result = []
  while decNo>0:
    remainder = decNo%2
    result.append(remainder)
    decNo = decNo//2
  return result[::-1]

def toBase(decNo, base):
  '''
  Improve it further to replace the characters
  greater than 9 with teh alphabets.
  '''
  result = []
  if base>16:
    print("Base value less than 16 is expected!")
    exit()
  try:  
    while decNo>0:
      remainder = decNo%base
      result.append(remainder)
      decNo = decNo//base
  except:
    print("error!")
    return
  return result[::-1]
 
def infix2postfix(expr):
  precedence = {'/':3, '*':3, '+':2, '-':2, '(':1}
  chars      = 'abcdefghijklmnopqrstuvwxyz'
  nos        = '0123456789'
  output      = []
  operatorStk = []
  exprI       = expr.split()
  for i in exprI:
    print("i ", i)
    if i in chars or i in nos:
      output.append(i)
      print("output1: ", output)
    elif i == '(':
      operatorStk.append(i)
      print("opSTK: ", operatorStk)
    elif i == ')':
      top_i  = operatorStk.pop()
      while top_i!='(':
        output.append(top_i)
        top_i  = operatorStk.pop()
    else:
      '''
      append all the operators and check their precedences
      '''
      while operatorStk and (precedence[operatorStk[-1]]>=precedence[i]):
        output.append(operatorStk.pop())
      output.append(i)
  while operatorStk:
    output.append(operatorStk.pop())
  return ''.join(output)
      
      
# test cases
a = ['s','t','r','i', 'n', 'g']
s = stack()
s.push('a')
s.push('b')
s.pop()
stk = ()
#print(validParenthesis2(stk))

#def test_validParen(in_, out_):
#    out = validParenthesis(in_)
#    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)

#def test_validParen2(in_, out_):
#    out = validParenthesis(in_)
#    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)
print(toBinary(42))
print(toBinary(25))
print(toBase(25, 16))
print(infix2postfix('A * B + C * D'))
def test_toBinary(in_, out_):
    out = toBinary(in_)
    assert out_ == out, "Expected " + str(out_) + ", found: " + str(out)

def run_tests():
  test_toBinary(42, [1, 0, 1, 0, 1, 1])
  test_toBinary(25, [1, 1, 1, 1, 1])
#    test_validParen('()', True)
#    test_validParen('(()', False)
  #  test_validParen2('(()}', True)
