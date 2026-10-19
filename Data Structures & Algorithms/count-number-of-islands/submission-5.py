from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == '1':
                    seen.add((i, j))
                    res += 1
                    q = deque([(i, j)])
                    while q:
                        x, y = q.popleft()
                        for dx, dy in directions:
                            nx = dx + x
                            ny = dy + y
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in seen and grid[nx][ny] == "1":
                                seen.add((nx, ny))
                                q.append((nx, ny))
        return res