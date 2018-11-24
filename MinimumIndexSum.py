#599. Minimum Index Sum of Two Lists
class Solution(object):
    def findRestaurant(self, list1, list2):
        dic    = {}
        result = []
        sumMin = float('inf')
       # summ = 0
        for idx, val in enumerate(list1):
            dic[val] = idx
            print("dic", dic)
        for idx, val in enumerate(list2):
            if val in dic:
                summ  = dic[val] + idx
                print("summ", summ)
                print("idx, dic[val], val", idx, dic[val], val)
                if summ < sumMin:
                    print("1", summ)
                    result = [val]
                    sumMin = summ
                elif summ == sumMin:
                    print("2", summ)
                    result.append(val)
        return result
            
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC", "BC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun", "BC"]     

s = Solution()
print(s.findRestaurant(list1, list2))
