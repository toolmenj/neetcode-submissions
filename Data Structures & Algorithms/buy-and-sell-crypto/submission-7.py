class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0  # buy point
        max_profit = 0

        for right in range(1, len(prices)):
            # increasing trend relative to buy price
            if prices[right] > prices[left]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            # Price dropped below buy price
            else:
                left = right

        return max_profit