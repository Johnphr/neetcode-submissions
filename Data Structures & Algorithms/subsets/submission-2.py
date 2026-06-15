class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        mySet = set()
        def backtract(l):
            if not l or tuple(l) in mySet:
                return
            res.append(l)
            mySet.add(tuple(l))
            for i in range(len(l)):
                backtract(l[0:i]+l[i+1:len(l)])
        backtract(nums)
        return res