class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charsC = {}
        for c in s1:
            charsC[c] = charsC.get(c, 0) + 1
        chars = charsC.copy()
        l = 0 
        r = 0
        while r < len(s2):
            if r - l >= len(s1):
                return True
            if s2[r] in chars:
                while chars[s2[r]] == 0:
                    if s2[l] in chars:
                        chars[s2[l]] += 1
                    l += 1
                chars[s2[r]] -= 1
                r += 1
            else:
                r += 1
                l = r
                chars = charsC.copy()
        if r - l >= len(s1):
                return True
        return False

            