class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        myList = 0
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][len(matrix[m]) - 1]:
                myList = m
                break
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        l = 0
        r = len(matrix[myList]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[myList][m] == target:
                return True
            elif target < matrix[myList][m]:
                r = m - 1
            else:
                l = m + 1
        return False
        