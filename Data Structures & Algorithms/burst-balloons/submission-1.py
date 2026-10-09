class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        coins = [1] + nums + [1]
        memo = {}
        def dp(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if l + 1 == r:
                return 0
            mC = 0
            for i in range(l + 1, r):
                c = coins[l] * coins[i] * coins[r] + dp(l, i) + dp(i, r)
                mC = max(mC, c)
            memo[(l, r)] = mC
            return memo[(l, r)]
        return dp(0, len(coins) - 1)