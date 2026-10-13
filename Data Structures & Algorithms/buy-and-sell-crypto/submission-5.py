class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrices = 0
        minBuy = prices[0]
        for sell in prices:
            maxPrices = max(maxPrices, sell-minBuy)
            minBuy = min(minBuy, sell)
        return maxPrices