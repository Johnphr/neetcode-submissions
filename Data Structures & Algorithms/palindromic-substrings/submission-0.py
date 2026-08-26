class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # Odd
            l = r = i
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
            # Even
            l = i
            r = i + 1
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
        return res
            