class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxV = 0
        while r < len(prices):
            maxV = max(maxV, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxV