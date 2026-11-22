class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        seen = set()
        def change(i, j, val):
            if (i, j) not in seen:
                seen.add((i, j))
                change(j, n - 1 - i, matrix[i][j])
            matrix[i][j] = val
        for i in range(n):
            for j in range(n):
                if (i, j) not in seen:
                    seen.add((i, j))
                    change(j, n - 1 - i, matrix[i][j])