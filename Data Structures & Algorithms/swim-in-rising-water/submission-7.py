import heapq
from collections import defaultdict
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        distances = defaultdict(lambda: float('inf'))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pq = []
        heapq.heappush(pq, (grid[0][0], 0, 0))
        distances[(0, 0)] = grid[0][0]
        while pq:
            dist, x, y = heapq.heappop(pq)
            for dx, dy in directions:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < n and 0 <= ny < n and max(dist, grid[nx][ny]) < distances[(nx, ny)]:
                    distances[(nx, ny)] = max(dist, grid[nx][ny])
                    heapq.heappush(pq, (distances[(nx, ny)], nx, ny))
        # print(distances)
        return distances[(n - 1, n - 1)]