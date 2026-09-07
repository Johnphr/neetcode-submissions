from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        myMap = {}
        inEdges = [0] * (numCourses + 1)
        for i in range(numCourses):
            myMap[i] = []
            inEdges[i] = 0

        for a, b in prerequisites:
            myMap[b].append(a)
            inEdges[a] += 1
        tempQ = []
        for i in range(numCourses):
            if inEdges[i] == 0:
                tempQ.append(i)
        q = deque(tempQ)
        res = 0
        while q:
            node = q.popleft()
            res += 1
            for conn in myMap[node]:
                inEdges[conn] -= 1
                if inEdges[conn] == 0:
                    q.append(conn)
        if res < numCourses:
            return False
        return True

        