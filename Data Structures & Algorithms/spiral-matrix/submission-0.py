class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        r = m - 1
        t = 0
        b = n - 1

        res = []

        while l <= r or t <= b:
            if t <= b:
                for i in range(l, r + 1):
                    res.append(matrix[t][i])
                t += 1
            if l <= r:
                for i in range(t, b + 1):
                    res.append(matrix[i][r])
                r -= 1
            if t <= b:
                for i in range(r, l - 1, -1):
                    res.append(matrix[b][i])
                b -= 1
            if l <= r:
                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
                l += 1
        
        return res
