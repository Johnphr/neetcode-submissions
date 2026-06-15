class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars = {}
        for i in range(len(t)):
            chars[t[i]] = chars.get(t[i], 0) + 1
        minSubstring = s
        l = 0
        passed = False
        for r in range(len(s)):
            if s[r] in chars:
                chars[s[r]] -= 1
            while all(val <= 0 for val in chars.values()):
                passed = True
                curSubstring = s[l:r+1]
                if len(curSubstring) < len(minSubstring):
                    minSubstring = curSubstring
                if s[l] in chars:
                    chars[s[l]] += 1           
                l += 1
        if not passed:
            return ""
        return minSubstring
