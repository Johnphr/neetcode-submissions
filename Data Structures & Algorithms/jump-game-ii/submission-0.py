class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return 0
            if i + nums[i] >= len(nums) - 1:
                return 1
            memo[i] = 10 ** 9
            for j in range(1, nums[i] + 1):
                memo[i] = min(memo[i], dp(i + j) + 1)
            return memo[i]
        return dp(0)