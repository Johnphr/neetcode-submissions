class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i, val):
            if (i, val) in memo:
                return memo[(i, val)]
            if val > amount or i >= len(coins):
                return 0
            if val == amount:
                return 1
            memo[(i, val)] = dp(i + 1, val) + dp(i, val + coins[i])
            return memo[(i, val)]
        return dp(0, 0)
        