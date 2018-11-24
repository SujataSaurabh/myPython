# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

class Solution():
  def maxProfit(self, prices):
    profit = 0
    for i in range(0, len(prices)-1):
      print("i", i)
      if prices[i+1] > prices[i]:
        print("prices[i] - prices[i-1]", prices[i+1] - prices[i])
        profit += (prices[i+1] - prices[i])
        print("profit ", profit)
    return profit
  
prices = [7, 1, 5, 3,6, 4]
prices1 = [1,2,3,4,5]
prices3 = [7,6,4,3,1]
s = Solution()
print(s.maxProfit(prices))
print(s.maxProfit(prices1))
print(s.maxProfit(prices3))
