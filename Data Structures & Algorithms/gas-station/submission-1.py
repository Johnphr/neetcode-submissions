class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curTot = 0
        if sum(gas) < sum(cost):
            return -1
        res = 0
        for i in range(len(gas)):
            curTot += gas[i] - cost[i]
            if curTot < 0:
                res = i + 1
                curTot = 0
        return res