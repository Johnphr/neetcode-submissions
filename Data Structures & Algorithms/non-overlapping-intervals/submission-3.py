class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for l, r in intervals[1:]:
            if l >= prevEnd:
                prevEnd = r
            else:
                res += 1
                prevEnd = min(prevEnd, r)
        return res