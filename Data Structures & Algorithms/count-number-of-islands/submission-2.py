from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    res += 1
                    q = deque([(i, j)])
                    while q:
                        x, y = q.popleft()
                        visited.add((x,y))
                        for d in directions:
                            if (0 <= (x + d[0]) < len(grid)) and (0 <= (y + d[1]) < len(grid[0])) and (x + d[0], y + d[1]) not in visited and grid[x + d[0]][y + d[1]] == "1":
                                q.append((x + d[0], y + d[1]))
        return res
