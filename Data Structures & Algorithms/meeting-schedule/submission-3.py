"""
Definition of Interval:
from types import MappingProxyType
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        newIntervals = []
        for inte in intervals:
            sta = inte.start
            en = inte.end
            newIntervals.append([sta, en])
        newIntervals.sort()
        for i in range(len(newIntervals) - 1):
            curInt = newIntervals[i]
            nextInt = newIntervals[i + 1]
            if curInt[1] > nextInt[0]:
                return False
        return True
