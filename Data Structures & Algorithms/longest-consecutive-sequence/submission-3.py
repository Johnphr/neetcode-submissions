class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        maxC = 0
        c = 0
        for n in nums:
            if n - 1 not in mySet:
                while n + c in mySet:
                    c += 1
                maxC = max(maxC, c)
            c = 0
        return maxC
                
