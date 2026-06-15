class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        q = None
        while l <= r:
            m = (r + l) // 2
            if target in set(matrix[m]):
                q = m
                break
            elif target > matrix[m][0]:
                l = m + 1
            else:
                r = m - 1
        if q == None:
            return False
        l = 0
        r = len(matrix[q]) - 1
        while l <= r:
            m = (r + l) // 2
            if target == matrix[q][m]:
                return True
            elif target > matrix[q][m]:
                l = m + 1
            else:
                r = m - 1
        return False
        
        