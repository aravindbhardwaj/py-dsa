from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return max_profit


sol = Solution()

#Test cases
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

print(sol.maxProfit(prices1)) # 5
print(sol.maxProfit(prices2)) # 0