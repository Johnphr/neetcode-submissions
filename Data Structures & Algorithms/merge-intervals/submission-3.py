class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        res = []
        while i < len(intervals):
            curInt = intervals[i]
            while i < len(intervals) and curInt[1] >= intervals[i][0]:
                curInt[0] = min(curInt[0], intervals[i][0])
                curInt[1] = max(curInt[1], intervals[i][1])
                i += 1
            res.append(curInt)
        return res
        