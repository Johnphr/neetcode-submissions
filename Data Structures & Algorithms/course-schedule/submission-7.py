class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        memo = {}
        def func(node, visited):
            if node in visited:
                memo[node] = False
                return memo[node]
            if node in memo:
                return memo[node]
            if node not in reqs:
                memo[node] = True
                return memo[node]
            for conn in adjList[node]:
                visited.add(node)
                res = func(conn, visited)
                visited.remove(node)
                memo[node] = res
                if not memo[node]:
                    break
            return memo[node]
        adjList = {}
        reqs = set()
        for a, b in prerequisites:
            reqs.add(a)
            if a not in adjList:
                adjList[a] = set([b])
            else:
                adjList[a].add(b)
        for req in reqs:
            if req in memo:
                myRes = memo[req]
            else:
                myRes = func(req, set())
            if not myRes:
                return False
        return True