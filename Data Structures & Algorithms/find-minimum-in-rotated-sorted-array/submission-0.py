class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        if nums[l] < nums[m] < nums[r]:
                return minVal
        while l <= r:
            m = (l + r) // 2
            if (nums[m] > nums[r]):
                if nums[m] < minVal:
                    minVal = nums[m]
                l = m + 1
            else:
                if nums[m] < minVal:
                    minVal = nums[m]
                r = m - 1
        return minVal
            
            

            
            
                
        