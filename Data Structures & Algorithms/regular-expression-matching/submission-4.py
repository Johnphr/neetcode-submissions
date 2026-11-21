class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        n = len(s)
        m = len(p)
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j >= m and i >= n:
                memo[(i, j)] = True
                return memo[(i, j)]

            memo[(i, j)] = False
            if j == m - 1 or (j < m - 1 and p[j + 1] != '*'):
                if i < n and (s[i] == p[j] or p[j] == "."):
                    memo[(i, j)] = dp(i + 1, j + 1)

            elif j < m - 1 and p[j + 1] == '*':
                k = i
                char = p[j]
                memo[(i, j)] = memo[(i, j)] or dp(k, j + 2)
                while k < n and (s[k] == char or char == '.'):
                    memo[(i, j)] = memo[(i, j)] or dp(k + 1, j + 2)
                    k += 1
                    
                     
            return memo[(i, j)]
        return dp(0, 0)