class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        for r in range(k - 1, len(nums)):
            window = nums[l:r+1]
            res.append(max(window))
            l += 1
        return res
        