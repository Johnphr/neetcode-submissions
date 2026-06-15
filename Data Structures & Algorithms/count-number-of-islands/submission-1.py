from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == "1":
                    q = deque([(i, j)])
                    visited.add((i, j))
                    while q:
                        x, y = q.popleft()
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx = x + dx
                            ny = y + dy
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] == "1":
                                visited.add((nx, ny))
                                q.append((nx, ny))
                    island_count += 1
        return island_count
        