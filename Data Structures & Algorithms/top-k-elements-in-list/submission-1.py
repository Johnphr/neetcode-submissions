class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        
        for n in nums:
            myDict[n] = myDict.get(n, 0) + 1
        tn = []
        for i in range(k):
            tn.append(max(myDict, key=myDict.get))
            myDict.pop(max(myDict, key=myDict.get))
        return tn
        
        