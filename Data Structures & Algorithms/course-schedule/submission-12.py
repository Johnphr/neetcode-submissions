from collections import deque

class Solution:      
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        in_degrees = {}

        for i in range(numCourses):
            adj[i] = []
            in_degrees[i] = 0

        for i,v in prerequisites:
            adj[v].append(i)
            in_degrees[i] += 1

        q = deque()
        visited = 0

        for i,e in in_degrees.items():
            if e == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            visited += 1
            for neighbor in adj[curr]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    q.append(neighbor)

        if visited == numCourses:
            return True
        else:
            return False



        