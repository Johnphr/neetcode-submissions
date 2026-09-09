class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        res = s / 2
        if s % 2 == 1:
            return False
        memo = {}
        def dp(curT, myList):
            if curT in memo:
                return memo[curT]
            if curT > res:
                return False
            if curT == res:
                return True
            memo[curT] = False
            for i in range(len(myList)):
                n = myList[i]
                temp = dp(curT + n, myList[0:i] + myList[i+1:len(myList)])
                if temp:
                    memo[curT] = True
                    break
            return memo[curT]
                
        return dp(0, nums)
            
        