class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            target = -nums[i]
            hashMap = {}
            for j in range(len(nums)):
                if j != i:
                    hashMap[nums[j]] = j
            for j in range(len(nums)):
                if j != i:
                    r = target - nums[j]
                    if r in hashMap and hashMap[r] != j:
                        l = [nums[i], nums[j], r]
                        # print(l)
                        l.sort()
                        res.add(tuple(l))
        return list(res)
        