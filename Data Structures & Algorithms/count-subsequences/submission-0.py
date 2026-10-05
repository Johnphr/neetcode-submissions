class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        lenS = len(s)
        lenT = len(t)
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j >= lenT:
                return 1
            if i >= lenS:
                return 0
            memo[(i, j)] = dp(i + 1, j)
            if s[i] == t[j]:
                memo[(i, j)] += dp(i + 1, j + 1)
            return memo[(i, j)]
        return dp(0, 0)