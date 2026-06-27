from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visited = set()
                    visited.add((i,j))
                    q = deque([(i, j, 1)])
                    while q:
                        x, y, l = q.popleft()
                        for d in directions:
                            nX = x + d[0]
                            nY = y + d[1]
                            if (0 <= nX < len(grid)) and (0 <= nY < len(grid[0])) and grid[nX][nY] > 0 and (nX, nY) not in visited:
                                grid[nX][nY] = min(l, grid[nX][nY])
                                visited.add((nX, nY))
                                q.append((nX, nY, l + 1))