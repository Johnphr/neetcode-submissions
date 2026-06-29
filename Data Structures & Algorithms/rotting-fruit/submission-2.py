from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = {}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visited[(i,j)] = 0
                elif grid[i][j] == 2:
                    visited[(i,j)] = 0
                    curVis = set()
                    q = deque([(i, j, 0)])
                    while q:
                        x, y, d = q.popleft()
                        for dx, dy in directions:
                            nX = x + dx
                            nY = y + dy
                            if (0 <= nX < len(grid)) and (0 <= nY < len(grid[0])) and grid[nX][nY] == 1 and (nX, nY) not in curVis:
                                curVis.add((nX, nY))
                                if (nX, nY) not in visited:
                                    visited[(nX, nY)] = d + 1
                                else:
                                    visited[(nX, nY)] = min(visited[(nX, nY)], d + 1)
                                q.append((nX, nY, d + 1))
        if len(visited) < len(grid) * len(grid[0]) or not visited:
            return -1
        print(len(visited))
        print(len(grid) * len(grid))
        theMax = max(visited.values())
        return theMax