class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 2)
        coinSet = set(coins)
        for i in range(1, amount + 1):
            if i in coinSet:
                dp[i] = 1
                continue
            minVal = 10 ** 9
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                    minVal = min(minVal, dp[i - coin] + 1)
            if minVal != (10 ** 9):
                dp[i] = minVal
            else:
                dp[i] = -1
        return dp[amount]