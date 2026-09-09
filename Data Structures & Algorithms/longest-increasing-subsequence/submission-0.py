class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def dp(i):
            if i in memo:
                return memo[i]
            if i == n - 1:
                return 1
            memo[i] = 1
            num = nums[i]
            for j in range(i + 1, n):
                if nums[j] > num:
                    memo[i] = max(memo[i], dp(j) + 1)
            return memo[i]
        res = 1
        for i in range(n):
            res = max(dp(i), res)
        return res
        