from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(1, len(edges) + 1):
            adj[i] = []
        for i in range(len(edges)):
            u, v = edges[i]
            adj[u].append(v)
            adj[v].append(u)
            q = deque([(u, -1)])
            seen = set()
            seen.add(u)
            res = False
            while q:
                node, prev = q.popleft()
                for conn in adj[node]:
                    if conn != prev:
                        if conn in seen:
                            res = True
                        else:
                            seen.add(conn)
                            q.append((conn, node))
            if res:
                return edges[i]
        