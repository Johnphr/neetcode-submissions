from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashMap = {}
        for a, b in edges:
            if a not in hashMap:
                hashMap[a] = []
            if b not in hashMap:
                hashMap[b] = []
            hashMap[a].append(b)
            hashMap[b].append(a)
        seen = set()
        q = deque([(0, 0)])
        seen.add(0)
        while q:
            camefrom, node = q.popleft()
            if node in hashMap:
                for conn in hashMap[node]:
                    if conn == camefrom:
                        continue
                    if conn in seen:
                        return False
                    seen.add(conn)
                    q.append((node, conn))
        if len(seen) < n:
            return False
        return True