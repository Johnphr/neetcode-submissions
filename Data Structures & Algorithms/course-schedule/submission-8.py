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
        seen = set()
        for i in range(numCourses):
            if inEdges[i] == 0:
                tempQ.append(i)
                seen.add(i)
        q = deque(tempQ)
        while q:
            node = q.popleft()
            for conn in myMap[node]:
                inEdges[conn] -= 1
                if inEdges[conn] == 0 and conn not in seen:
                    seen.add(conn)
                    q.append(conn)
        if len(seen) < numCourses:
            return False
        return True

        