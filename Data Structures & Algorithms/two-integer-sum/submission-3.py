class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range(len(nums)):
            myMap[nums[i]] = i
        for i in range(len(nums)):
            dif = target - nums[i] 
            if dif in myMap and myMap[dif] != i:
                return [i, myMap[dif]]