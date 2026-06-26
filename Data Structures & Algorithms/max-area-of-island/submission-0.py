from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    q = deque([(i, j)])
                    visited.add((i, j))
                    newArea = 1
                    while q:
                        x, y = q.popleft()
                        for d in directions:
                            nX = x + d[0]
                            nY = y + d[1]
                            if (0 <= nX < len(grid)) and (0 <= nY < len(grid[0])) and grid[nX][nY] == 1 and (nX, nY) not in visited:
                                visited.add((nX, nY))
                                q.append((nX, nY))
                                newArea += 1
                    res = max(res, newArea)
        return res
