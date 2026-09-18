class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curTot = 0
        for num in nums:
            if curTot < 0:
                curTot = 0
            curTot += num
            res = max(res, curTot)
        return res
