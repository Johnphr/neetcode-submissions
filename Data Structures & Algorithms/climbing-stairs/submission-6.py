class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            memo[n] = dp(n - 1) + dp(n - 2) 
            return memo[n]
        return dp(n)