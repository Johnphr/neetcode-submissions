from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        count = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                count += 1
                seen.add(i)
                q = deque([i])
                while q:
                    node = q.popleft()
                    for conn in adj[node]:
                        if conn not in seen:
                            seen.add(conn)
                            q.append(conn)
        return count
        