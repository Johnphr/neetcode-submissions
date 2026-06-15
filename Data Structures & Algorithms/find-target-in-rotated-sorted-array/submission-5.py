class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # Condition to go to the right
            elif (nums[m] > nums[r] and not(nums[l] <= target < nums[m])) or (nums[m] < nums[r] and (nums[m] < target <= nums[r])):
                l = m + 1
            else:
                r = m - 1
        return -1