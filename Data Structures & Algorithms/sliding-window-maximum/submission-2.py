class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        res = []
        for i in range(r, len(nums) + 1, 1):
            res.append(max(nums[l:i]))
            l += 1
        return res