class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        for i in range(len(nums)):
            seek = target - nums[i]
            if seek in hashMap and hashMap[seek] != i:
                return [i, hashMap[seek]]