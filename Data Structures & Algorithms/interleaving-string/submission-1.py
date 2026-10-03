class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def dp(i, j):
            k = i + j
            if (i, j) in memo:
                return memo[(i, j)]
            if k >= len(s3):
                return True
            memo[(i, j)] = False
            if i < len(s1) and s1[i] == s3[k]:
                memo[(i, j)] = memo[(i, j)] or dp(i + 1, j)
            if j < len(s2) and s2[j] == s3[k]:
                memo[(i, j)] = memo[(i, j)] or dp(i, j + 1)
            return memo[(i, j)]
        return dp(0, 0)
