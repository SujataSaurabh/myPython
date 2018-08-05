#	@SuGo, 5 August, 2018
#	Python implementation of queue and stack 
#	
from collections import deque
#	-- STACK (LIFO)  --

stk = []
# insert element in stack

stk.append("one")
stk.append(2)
print("\n ----  STACK (LIFO)  ----")
print("Full stack is::  ", stk)
print("First pop():: ", stk.pop(), "\n")
 
#	-- QUEUE (FIFO) -- 
que = []
que.insert(0, "two")
que.insert(1, "three")
que.insert(2, "four")
print("\n ---  QUEUE ----")
print("Queue:: ", que)
print("Queue pop():: ", que.pop(), "\n")

#	-- DEQUEUE (FIFO) --
dque =deque([]) 
dque.append("one")
dque.append("two")
dque.append("four")
print("\n---- QUEUE (FIFO) ----")
print("DQUE:: ",dque)
print("DQUE pop:: ", dque.popleft())
print("DQUE pop2:: ", dque.popleft(), "\n")
