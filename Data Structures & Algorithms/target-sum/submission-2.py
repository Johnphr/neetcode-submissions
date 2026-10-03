class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for i in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(len(nums)):
            for key, value in dp[i].items():
                dp[i + 1][key + nums[i]] += value
                dp[i + 1][key - nums[i]] += value
        return dp[len(nums)][target]