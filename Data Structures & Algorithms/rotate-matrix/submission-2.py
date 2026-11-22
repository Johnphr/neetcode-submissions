class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        def change(i, j, val, c):
            if c < 4:
                change(j, n - 1 - i, matrix[i][j], c + 1)
            matrix[i][j] = val
        for i in range(n//2 + n % 2):
            for j in range(i, n - 1 - i):
                change(j, n - 1 - i, matrix[i][j], 1)