class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        maxR = height[r]
        maxL = height[l]
        res = 0
        while l < r:
            if maxR > maxL:
                res += maxL - height[l]
                l += 1
                maxL = max(maxL, height[l])
            else:
                res += maxR - height[r]
                r -= 1
                maxR = max(maxR, height[r])
        return res
        