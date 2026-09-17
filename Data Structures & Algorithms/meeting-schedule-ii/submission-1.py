"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        newIntervals = []
        for inte in intervals:
            newIntervals.append([inte.start, inte.end])
        newIntervals.sort()
        i = 1
        pq = [newIntervals[0][1]]
        heapq.heapify(pq)
        res = 1
        while (i < len(newIntervals)):
            curStart = newIntervals[i][0]
            curEnd = newIntervals[i][1]
            if curStart >= pq[0]:
                while pq and curStart >= pq[0]:
                    heapq.heappop(pq)
                heapq.heappush(pq, curEnd)
            else:
                heapq.heappush(pq, curEnd)
                res = max(res, len(pq))
            i += 1

        
        return res