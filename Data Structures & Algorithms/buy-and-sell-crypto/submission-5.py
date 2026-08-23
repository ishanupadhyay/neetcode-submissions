class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0

        for i in range(0, len(prices)):
            j = i
            while j < len(prices):
                if prices[j] > prices[i]:
                    currentprofit = prices[j] - prices[i]
                    maxprofit = max(currentprofit, maxprofit)
                j += 1
            
        return maxprofit
