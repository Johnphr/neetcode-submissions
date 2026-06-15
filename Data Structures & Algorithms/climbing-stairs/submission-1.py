class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(num):
            if num in memo:
                return memo[num]
            if num < 2:
                answer = 1
            else:
                answer = dp(num - 1) + dp(num - 2)
            memo[num] = answer
            return answer
        return dp(n)
