class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r =  len(height) - 1
        maxL = maxR = 0
        water = 0
        while l < r:
            hL = height[l]
            hR = height[r]
            maxR = max(maxR, hR)
            maxL = max(maxL, hL)
            if maxR < maxL:
                water += maxR - hR
                r -= 1
                print("Water", water, l, r)
            else:
                water += maxL - hL
                l += 1
                print("Water", water, l, r)
        return water
            