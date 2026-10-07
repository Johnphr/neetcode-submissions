class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
        for i in range(l2):
            dp[l1][i] = l2 - i
        for j in range(l1):
            dp[j][l2] = l1 - j
        # print(dp)
        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i + 1][j] + 1, dp[i][j + 1] + 1, dp[i + 1][j + 1] + 1)
        return dp[0][0]


        ''' def dp(i, j):
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
        return dp(0, 0) '''