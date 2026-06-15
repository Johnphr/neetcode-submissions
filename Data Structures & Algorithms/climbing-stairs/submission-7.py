class Solution:
    def climbStairs(self, n: int) -> int:
        ''' memo = {}
        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            memo[n] = dp(n - 1) + dp(n - 2) 
            return memo[n]
        return dp(n) '''
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 
        for i in range(2, n + 1, 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]