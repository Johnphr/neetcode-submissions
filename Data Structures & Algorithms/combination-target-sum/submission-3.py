class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        seen = set()
        res = []
        def backtrack(curT, l):
            nonlocal res
            if curT < 0:
                return
            for i in range(len(nums) -1, -1, -1):
                if nums[i] > curT:
                    continue
                goofy = l + [nums[i]] 
                goofy.sort()
                if nums[i] == curT and goofy not in res:
                    res.append(goofy)
                elif nums[i] < target and tuple(goofy) not in seen:
                    seen.add(tuple(goofy))
                    backtrack(curT - nums[i], goofy)
                    
        backtrack(target, [])
        return res