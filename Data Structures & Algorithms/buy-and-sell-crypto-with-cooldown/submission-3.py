class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, canBuy, val):
            # print(i, canBuy, val)
            if (i, canBuy, val) in memo:
                return memo[(i, canBuy, val)]
            if i >= len(prices):
                return val
            if canBuy:
                memo[(i, canBuy, val)] = max(dp(i + 1, False, val - prices[i]), dp(i + 1, True, val))
            else:
                memo[(i, canBuy, val)] = max(dp(i + 2, True, val + prices[i]), dp(i + 1, False, val))
            return memo[(i, canBuy, val)]
        dp(0, True, 0)
        return memo[(0, True, 0)]