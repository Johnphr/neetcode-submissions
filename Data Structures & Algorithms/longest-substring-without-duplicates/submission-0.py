class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        r = 0
        maxLength = 1
        curLength = 1
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                curLength += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    curLength -= 1
                    l += 1
            maxLength = max(maxLength, curLength)
        return maxLength - 1


        