class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(n):
            if n in memo:
                return memo[n]
            if n == 1:
                answer = 1
            elif n == 2:
                answer = 2
            else:
                answer = dp(n - 1) + dp(n - 2)
            memo[n] = answer
            return answer
        
        return dp(n)