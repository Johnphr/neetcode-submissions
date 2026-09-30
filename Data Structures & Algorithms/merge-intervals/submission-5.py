class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        curInterval = intervals[0]
        for l, r in intervals:
            if l <= curInterval[1]:
                curInterval[0] = min(curInterval[0], l)
                curInterval[1] = max(curInterval[1], r)
            else:
                res.append(curInterval)
                curInterval = [l, r]
        res.append(curInterval)
        return res