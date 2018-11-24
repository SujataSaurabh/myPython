class Solution():
  def firstUniqChar(self, s):
    dictionary = {}
    returnInd = len(s)
    print("dict 1 ", dictionary)
    flag       = 0 
    for ind, item in enumerate(s):
      if item in dictionary:
        dictionary[item] = -1
        print("dict 2 ", dictionary)
      else:
        dictionary[item] = ind
        print("dict 3 ", dictionary)
    
    for item in dictionary:
      print("item 1", item)
      if dictionary[item]!= -1:
        print("dict[item] ", dictionary[item])
        if returnInd > dictionary[item]:
          flag = 1
          returnInd  = dictionary[item]
          print("returnInd ", returnInd)
          #
  def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = len(s)
        c = "abcdefghijklmnopqrstuvwxyz"
        for x in c:
            m = s.find(x)
            print("m and x", m, x)
            if m != -1:
                n = s.rfind(x)
                print("m, n, x ", m,n,x)
                if m==n:
                    res = min(res,n)
                    print("res ", res)
        return (res if res<len(s) else -1) 
s = "leet"
sol = Solution()
print(sol.firstUniqChar1(s))
