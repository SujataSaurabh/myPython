class Solution():
  def reverse(self, x):
    reverse = 0
    y = abs(x)
    while y:
      a = y%10  # remainder
      y = y//10  # quotient
      reverse = reverse * 10 + a 
    return (-1*reverse) if x<0 else reverse
    
  def reverseInt(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
    
        reverse = 0
    
        y = abs(x)
        while y:
          a = y%10  # remainder
          y = y//10  # quotient
          # check for the 32 bit signed integer range
          if(reverse > (MAX_INT//10) or  (reverse == MAX_INT//10  and a > 7)):
            print("1 true")
            return 0
          if(reverse< (MIN_INT//10) or  (reverse == MIN_INT//10  and a < -8)):
            print("2 true")
            return 0 
          reverse = reverse * 10 + a
        return (-1*reverse) if x<0 else reverse
x = -231
s = Solution()
print(s.reverseInt(x))
