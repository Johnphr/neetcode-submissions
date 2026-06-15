class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mySDict = {}
        myTDict = {}

        for c in s:
            mySDict[c] = mySDict.get(c, 0) + 1
        for c in t:
            myTDict[c] = myTDict.get(c, 0) + 1

        if mySDict == myTDict:
            return True
        return False
        
        
        