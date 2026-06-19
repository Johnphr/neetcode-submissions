class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        mySet = set()
        res = []
        subset = []
        def backtrack(i):
            nonlocal mySet
            nonlocal res
            nonlocal subset
            realSub = subset.copy()
            realSub.sort()
            if i >= len(nums) and tuple(realSub) not in mySet:
                res.append(realSub.copy())
                mySet.add(tuple(realSub.copy()))
                return
            if i >= len(nums):
                return
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)
        backtrack(0)
        return res
        