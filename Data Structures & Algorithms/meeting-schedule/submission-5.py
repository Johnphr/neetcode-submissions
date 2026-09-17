"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        tupleIntervals = []
        for el in intervals:
            tupleIntervals.append((el.start, el.end))
        tupleIntervals.sort()
        prevEnd = tupleIntervals[0][1]
        for start, end in tupleIntervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                return False
        return True