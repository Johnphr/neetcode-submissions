class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        l1 = len(word1)
        l2 = len(word2)
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= l1:
                return l2 - j
            if j >= l2:
                return l1 - i
            memo[(i, j)] = 0
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i + 1, j + 1)
            else:
                memo[(i, j)] = min(dp(i + 1, j) + 1, dp(i, j + 1) + 1, dp(i + 1, j + 1) + 1)
            return memo[(i, j)]
        return dp(0, 0)