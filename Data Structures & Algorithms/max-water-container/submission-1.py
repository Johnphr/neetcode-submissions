class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxA = 0
        while l < r:
            minLocal = min(heights[l], heights[r])
            area = minLocal * (r - l)
            maxA = max(area, maxA)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxA

        