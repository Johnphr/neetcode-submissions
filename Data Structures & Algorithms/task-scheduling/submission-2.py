import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        myMap = {}
        for task in tasks:
            if task not in myMap:
                myMap[task] = 0
            myMap[task] += 1
        pq = [-c for c in myMap.values()]
        heapq.heapify(pq)
        q = deque()
        while pq or q:
            time += 1

            if pq:
                c = 1 + heapq.heappop(pq)
                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(pq, q.popleft()[0])
        return time