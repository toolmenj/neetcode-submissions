class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0  # 買入日（波段低點）
        max_profit = 0

        for right in range(1, len(prices)):
            # 價格高於買入價 -> 處於遞增/獲利波段，更新最大獲利
            if prices[right] > prices[left]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            # 價格低於或等於買入價 -> 遇到更低點，重置買入點
            else:
                left = right

        return max_profit