class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxCount = 0
        count = 0
        for i in range(0, len(nums)):
            num = nums[i]
            if num - 1 not in nums_set:
                count = 1
                while num + 1 in nums_set:
                    count += 1
                    num += 1
            if count > maxCount:
                maxCount = count
            count = 0
        return maxCount

                
