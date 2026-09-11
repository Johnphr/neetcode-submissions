class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        res = 0
        intervals.sort()
        curInt = intervals[0]
        maxR = curInt[1]
        for i in range(1, len(intervals)):
            l, r = intervals[i]
            if l >= maxR:
                maxR = r
            else:
                res += 1
                maxR = min(maxR, r)
        return res