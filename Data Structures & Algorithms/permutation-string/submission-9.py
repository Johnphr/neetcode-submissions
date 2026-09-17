class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        limit = [0] * 26
        for c in s1:
            limit[ord(c)-ord('a')] += 1
        l = 0
        for r in range(len(s2)):
            c = s2[r]
            limit[ord(c)-ord('a')] -= 1
            if limit[ord(c)-ord('a')] < 0:
                while limit[ord(c)-ord('a')] < 0:
                    char = s2[l]
                    limit[ord(char)-ord('a')] += 1
                    l += 1
            if all(val == 0 for val in limit):
                return True
        return False
        