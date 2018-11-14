#	SuGo, 28 August 2018
class Solution():
  def reverse(self, x):
    reverse = 0
    y = abs(x)
    while y:
      a = y%10  # remainder
      y = y//10  # quotient
      reverse = reverse * 10 + a
      
    
    return (-1*reverse) if x<0 else reverse

x = -231
s = Solution()
print(s.reverse(x))
