class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Create the outside hashMap to group anagrams
        hashMap = {}
        for s in strs:
            # 2. Create the individual hashMap for each word
            indHash = [0] * 26
            for c in s:
                indHash[ord(c)-ord('a')] += 1 # 3. Hash the characters in s
            # 4. Hash the Hash by tuple
            tHash = tuple(indHash)
            # 5. Only create group if noneexistent.
            if tHash not in hashMap:
                hashMap[tHash] = [s]
            else:
                hashMap[tHash].append(s)
        # 6. Create the res
        res = []
        for l in hashMap.values():
            res.append(l)
        return res
