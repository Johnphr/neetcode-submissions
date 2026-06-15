class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ''' memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            if i <= 1:
                answer = cost[i]
            else:
                answer = min(dp(i - 1), dp(i - 2)) + cost[i]
            memo[i] = answer
            print(answer)
            return answer

        return min(dp(len(cost) - 1), dp(len(cost) - 2)) '''

        dp = [0] * (len(cost))

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[len(cost) - 1], dp[len(cost) - 2])

