class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i in range(len(nums)):
            myDict[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in myDict and myDict[diff] != i:
                return [i, myDict[diff]]


        