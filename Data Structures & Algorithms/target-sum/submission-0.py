class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)
        def dp(i, curTot):
            if (i, curTot) in memo:
                return memo[(i, curTot)]
            if i == n and curTot == target:
                return 1
            if i == n:
                return 0
            memo[(i, curTot)] = dp(i + 1, curTot + nums[i]) + dp(i + 1, curTot - nums[i])
            return memo[(i, curTot)]
        return dp(0, 0)