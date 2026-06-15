class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        for i in range(k, len(nums) + 1, 1):
            res.append(max(nums[l:i]))
            l += 1
        return res