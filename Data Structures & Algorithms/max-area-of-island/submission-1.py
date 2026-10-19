from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if (i, j) not in seen and grid[i][j] == 1:
                    seen.add((i, j))
                    curArea = 0
                    q = deque([(i, j)])
                    while q:
                        x, y = q.popleft()
                        curArea += 1
                        for dx, dy in directions:
                            nx = dx + x
                            ny = dy + y
                            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in seen and grid[nx][ny] == 1:
                                seen.add((nx, ny))
                                q.append((nx, ny))
                    res = max(res, curArea)
        return res