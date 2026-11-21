class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [] 
        i = 0
        while i < len(intervals):
            curInt = intervals[i]
            i += 1            
            while i < len(intervals) and intervals[i][0] <= curInt[1]:
                start, end = intervals[i][0], intervals[i][1]
                curInt[0] = min(start, curInt[0])
                curInt[1] = max(end, curInt[1])
                i += 1
            res.append(curInt)
        return res