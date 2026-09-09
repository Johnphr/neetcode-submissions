from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        hashMap = {}
        n = len(heights)
        m = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = []
        for i in range(n):
            for j in range(m):
                q = deque([(i, j)])
                seen = set()
                isPacific = False
                isAtlantic = False
                while q:
                    x, y = q.popleft()
                    if x == 0 or y == 0:
                        isPacific = True
                    if x == n - 1 or y == m - 1:
                        isAtlantic = True
                    for dx, dy in directions:
                        nx = dx + x
                        ny = dy + y
                        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in seen and heights[nx][ny] <= heights[x][y]:
                            seen.add((nx, ny))
                            q.append((nx, ny))
                if isPacific and isAtlantic:
                    res.append([i, j])
        return res
                    
                    

