class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l = 0
        r = 0
        maxSub = 0
        curSub = 0
        while r < len(s):
            if s[r] not in mySet:
                mySet.add(s[r])
                curSub += 1
                r += 1
            else:
                while s[r] in mySet:
                    mySet.remove(s[l])
                    curSub -= 1
                    l += 1
            maxSub = max(maxSub, curSub)
        return maxSub

