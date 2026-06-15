class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        output = []
        for i in range(len(nums)):
            l = 0
            left.append(1)
            while l < i:
                left[i] *= nums[l]
                l += 1
            r = len(nums) - 1
            right.append(1)
            while r > i:
                right[i] *= nums[r]
                r -= 1
            output.append(1)
            output[i] *= left[i] * right[i]
        return output

            
        