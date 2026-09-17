"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        points = []
        for inte in intervals:
            points.append([inte.start, 1])
            points.append([inte.end, 0])
        points.sort()
        res = 1
        count = 0
        for point in points:
            if point[1] == 1:
                count += 1
            else:
                count -= 1
            res = max(res, count)
        return res
