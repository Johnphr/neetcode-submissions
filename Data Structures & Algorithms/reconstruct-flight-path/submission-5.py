class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for u, v in sorted(tickets)[::-1]:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
        res = []
        stack = ["JFK"]
        while stack:
            cur = stack[-1]
            if not adj[cur]:
                res.append(stack.pop())
            else:
                stack.append(adj[cur].pop())
        return res[::-1]