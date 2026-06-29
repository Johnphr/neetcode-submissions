class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if not nums:
            return 0
        if n <= 3:
            return max(nums)
        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        alt = [0] * (n)
        alt[0] = nums[n - 1]
        alt[1] = max(nums[n - 1], nums[0])
        for i in range(2, n):
            alt[i] = max(alt[i - 1], alt[i - 2] + nums[i - 1])
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return max(dp[-2], alt[-2])