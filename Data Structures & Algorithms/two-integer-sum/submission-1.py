class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i, n in enumerate(nums):
            indexes[n] = i
        
        for i, n in enumerate(nums):
            dif = target - n
            if dif in indexes and indexes[dif] != i:
                return [i, indexes[dif]]

        