class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, canBuy):
            # print(i, canBuy, val)
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]
            if i >= len(prices):
                return 0
            if canBuy:
                memo[(i, canBuy)] = max(dp(i + 1, False) -prices[i], dp(i + 1, True))
            else:
                memo[(i, canBuy)] = max(dp(i + 2, True) + prices[i], dp(i + 1, False))
            return memo[(i, canBuy)]
        dp(0, True)
        return memo[(0, True)]