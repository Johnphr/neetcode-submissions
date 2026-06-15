class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        for i in range(len(nums)):
            n = target - nums[i]
            if n in hashMap and hashMap[n] != i:
                return [i, hashMap[n]]