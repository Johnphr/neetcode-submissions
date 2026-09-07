class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashMap = {}
        inEdges = [0] * (numCourses + 1)
        for i in range(numCourses):
            hashMap[i] = []
        for a, b in prerequisites:
            hashMap[b].append(a)
            inEdges[a] += 1
        q = deque()
        res = []
        for i in range(numCourses):
            if inEdges[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            res.append(node)
            for conn in hashMap[node]:
                inEdges[conn] -= 1
                if inEdges[conn] == 0:
                    q.append(conn)

        if len(res) < numCourses:
            return []
        return res