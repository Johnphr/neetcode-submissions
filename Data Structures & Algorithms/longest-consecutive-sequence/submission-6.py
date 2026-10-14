class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mySet = set(nums)
        res = 0
        

        for n in mySet:
            if n - 1 not in mySet:
                count = 0
                temp = n
                while temp in mySet:
                    count += 1
                    temp += 1
                res = max(res, count)
        return res
