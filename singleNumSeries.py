class Solution():
  def singleNumI(self, Arr):
    '''
    non-empty array of integers, every element appears twice except for one. Find that single one.
    '''
    return sum(set(Arr))*2 - sum(Arr)
  
  def singleNumII(self,Arr):
    '''
    Every element appears 3 times except for one which appears exactly once. Find the single one. 
    '''
    return (sum(set(Arr))*3 - sum(Arr))//2
  
  def singleNumII_hash(self, Arr):
    hashMap = {}
    for item in A:
      if item in hashMap:
        val = hashMap[item]
        val+= 1
        hashMap[item] = val
      else:
        hashMap[item] = 1
      
    for item, c in hashMap.items():
      if c == 1:
        return item
      
  def singleNumIII(self, Arr):  
    '''
    Every element appears twice except two elements which appear only once. Find those two elements
    USE HASHMAP
    '''
    print("coming soon...")
    
A = [2,2,3,2]
s = Solution()
print(s.singleNumII_hash(A))
