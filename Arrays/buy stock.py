from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy , sell = 0 , 1
        maxP = 0

        while sell < len(prices):
            if prices[sell] > prices[buy] :
                profit = prices[sell] - prices[buy]
                maxP = max(maxP , profit)

            else :
                buy = sell

            sell += 1

        return maxP

c1 = Solution()
print(c1.maxProfit([7,1,5,3,6,4]))

