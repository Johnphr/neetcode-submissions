class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def backtrack(small):
            if len(small) <= 0:
                res.append(sub.copy())
                return
            for i in range(len(small)):
                sub.append(small[i])
                backtrack(small[0:i] + small[i+1:len(small)])
                sub.pop()
        backtrack(nums)
        return res