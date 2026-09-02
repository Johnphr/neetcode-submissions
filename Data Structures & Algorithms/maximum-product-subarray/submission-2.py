class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 1
        curMin = 1
        for i in range(len(nums)):
            temp = max(nums[i], curMax * nums[i], curMin * nums[i])
            curMin = min(nums[i], curMax * nums[i], curMin * nums[i])
            curMax = temp
            res = max(res, curMax)
        return res