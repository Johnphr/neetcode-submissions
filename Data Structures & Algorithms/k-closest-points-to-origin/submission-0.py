import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []
        for i in range(len(points)):
            d = (points[i][0] ** 2 + points[i][1] ** 2) ** 0.5
            distances.append([d, points[i]])
        heapq.heapify(distances)
        for i in range(k):
            res.append(heapq.heappop(distances)[1])
        return res
        
        