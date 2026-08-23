class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            maxprofit = max(profit, maxprofit)

        return maxprofit
