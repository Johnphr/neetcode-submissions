class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(num):
            nonlocal n
            if num in memo:
                return memo[num]
            answer = 0
            if num < 2:
                answer = 1
            else:
                answer = dp(num - 1) + dp(num - 2)
            memo[num] = answer
            return answer
        dp(n)
        return memo[n]
