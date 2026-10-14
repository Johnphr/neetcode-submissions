class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Initialize empty hashmap for s and t
        hashS = [0] * 26
        hashT = [0] * 26

        # 2. Count characters in s and t.
        for c in s:
            hashS[ord(c)-ord('a')] += 1
        for c in t:
            hashT[ord(c)-ord('a')] += 1

        # 3. If any character it's extra.
        for i in range(26):
            if hashS[i] != hashT[i]:
                return False
        return True