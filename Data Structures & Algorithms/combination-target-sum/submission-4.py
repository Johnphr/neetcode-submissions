class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(curT, stack, ind):
            if curT == 0:
                res.append(list(stack))
                return
            for i in range(ind, len(nums), 1):
                if nums[i] > curT:
                    break
                stack.append(nums[i])
                backtrack(curT - nums[i], stack, i)
                stack.pop()
                    
        backtrack(target, [], 0)
        return res