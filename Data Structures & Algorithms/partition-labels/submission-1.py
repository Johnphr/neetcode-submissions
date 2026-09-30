class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        size = 0
        end = 0
        lastOcc = {}
        for i in range(len(s)):
            lastOcc[s[i]] = i
        for i in range(len(s)):
            c = s[i]
            end = max(end, lastOcc[c])
            if end <= i:
                res.append(size + 1)
                size = 0
            else:
                size += 1
        return res