class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        def dp(arr):
            tarr = tuple(arr)
            n = len(tarr)
            if tarr in memo:
                return memo[tarr]
            if len(arr) <= 0:
                return 0
            if len(arr) == 1:
                return arr[0]
            memo[tarr] = dp(arr[1:]) + arr[0] * arr[1]
            for i in range(1, n - 1):
                memo[tarr] = max(memo[tarr], dp(arr[0:i] + arr[i + 1:n]) + arr[i - 1] * arr[i] * arr[i + 1])
            memo[tarr] = max(memo[tarr], dp(arr[0:n - 1]) + arr[-1] * arr[-2])
            return memo[tarr]
        return dp(nums)
                