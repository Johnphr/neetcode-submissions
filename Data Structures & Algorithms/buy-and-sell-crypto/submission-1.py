class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxV = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                maxV = max(maxV, prices[j] - buy)
        return maxV