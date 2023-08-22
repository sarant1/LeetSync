class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = 0 
        high = 0
        for i in range(len(prices)):
            if prices[i] < prices[low]:
                low = i
                high = i
            if prices[i] > prices[high]:
                high = i
            profit = max(profit, prices[high]-prices[low])
        return profit


