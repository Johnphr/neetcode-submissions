import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        dist = {}
        for i in range(1, n + 1):
            adj[i] = []
            dist[i] = -1
        for u, v, t in times:
            adj[u].append((t, v))
        dist[k] = 0
        pq = [(0, k)]
        heapq.heapify(pq)
        while pq:
            di, node = heapq.heappop(pq)
            for w, conn in adj[node]:
                if dist[conn] == -1 or di + w < dist[conn]:
                    dist[conn] = di + w
                    heapq.heappush(pq, (w + di, conn))
        if min(dist.values()) == -1:
            return -1
        return max(dist.values())
        