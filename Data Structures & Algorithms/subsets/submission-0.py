class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(l):
            nonlocal res
            if l not in res:
                res.append(l)
            else:
                return
            for i in range(len(l)):
                backtrack(l[0:i] + l[(i + 1):len(l)])
        backtrack(nums)
        return res
        