class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = -10 ** 9
        curTot = 0
        i = 0
        while (i < len(nums)):
            if nums[i] >= 0:
                curTot += nums[i]
            else:
                if i == len(nums) - 1:
                    break
                elif curTot + nums[i] >= nums[i + 1]:
                    curTot += nums[i]
                else:
                    curTot = max(nums[i + 1], curTot + nums[i] + nums[i + 1])
                    i += 1
            i += 1
            res = max(res, curTot)
        return res

        