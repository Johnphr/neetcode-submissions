class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l = 0
        res = 0
        for r in range(1, len(prices)):
            while prices[l] > prices[r] and l < r:
                l += 1
            res = max(res, prices[r] - prices[l])
        return res
        