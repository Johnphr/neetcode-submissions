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
                        if x > 0 and (x - 1, y) not in visited and grid[x - 1][y] == "1":
                            visited.add((x - 1, y))
                            q.append((x - 1, y))
                        if x < len(grid) - 1 and (x + 1, y) not in visited and grid[x + 1][y] == "1":
                            visited.add((x + 1, y))
                            q.append((x + 1, y))
                        if y > 0 and (x, y - 1) not in visited and grid[x][y - 1] == "1":
                            visited.add((x, y - 1))
                            q.append((x, y - 1))
                        if y < len(grid[x]) - 1 and (x, y + 1) not in visited and grid[x][y + 1] == "1":
                            visited.add((x, y + 1))
                            q.append((x, y + 1))
                    island_count += 1
        return island_count
        