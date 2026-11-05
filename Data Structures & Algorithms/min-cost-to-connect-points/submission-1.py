import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                heapq.heappush(heap, (abs(x1-x2) + abs(y1-y2), (x1, y1, x2, y2)))
        finSize = len(points) - 1
        tot = 0
        cnt = 0
        parent = {(x, y): (x, y) for x, y in points}

        def find(p):
            while parent[p] != p:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
            
        while cnt < finSize:
            val, pts = heapq.heappop(heap)
            p1 = (pts[0], pts[1])
            p2 = (pts[2], pts[3])
            root1, root2 = find(p1), find(p2)
            if root1 != root2:
                parent[root1] = root2
                cnt += 1
                tot += val
            
        return tot