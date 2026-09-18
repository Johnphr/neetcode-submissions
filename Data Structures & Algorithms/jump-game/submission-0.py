class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(nums) - 1 or nums[i] >= len(nums) - 1 - i:
                return True
            memo[i] = False
            for j in range(1, nums[i] + 1):
                memo[i] = memo[i] or dp(i + j)
            return memo[i]
        return dp(0) 