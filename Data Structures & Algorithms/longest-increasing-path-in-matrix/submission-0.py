class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(matrix)
        m = len(matrix[0])
        memo = {}
        res = 0
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = 1
            for di, dj in directions:
                ni = di + i
                nj = dj + j
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]:
                    memo[(i, j)] = max(memo[(i, j)], dp(ni, nj) + 1)
            return memo[(i, j)]
        for i in range(n):
            for j in range(m):
                res = max(res, dp(i, j))
        return res