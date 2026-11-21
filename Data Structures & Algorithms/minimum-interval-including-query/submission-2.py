import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        vals = {}

        pq = []
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i][0], intervals[i][1]
                heapq.heappush(pq, (end - start + 1, end))
                i += 1
            # print(pq)
            while pq and pq[0][1] < q:
                heapq.heappop(pq)
            if pq:
                vals[q] = pq[0][0]
            else:
                vals[q] = -1
        return [vals[q] for q in queries]
        