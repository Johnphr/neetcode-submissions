class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s
            res += 'ó'
        return res
            
    def decode(self, s: str) -> List[str]:
        res = []
        prevI = -1
        for i in range(len(s)):
            if s[i] == 'ó':
                res.append(s[prevI+1:i])
                prevI = i
        return res