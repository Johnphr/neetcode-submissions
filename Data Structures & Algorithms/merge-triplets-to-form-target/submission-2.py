class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curT = triplets[0]
        start = 0
        while start < len(triplets) and (curT[0] > target[0] or curT[1] > target[1] or curT[2] > target[2]):
            start += 1
            try:
                curT = triplets[start]
            except IndexError:
                return False
        for i in range(start, len(triplets)):
            a = triplets[i][0]
            b = triplets[i][1]
            c = triplets[i][2]
            if curT == target:
                return True
            if a <= target[0] and b <= target[1] and c <= target[2]:
                curT = [max(a, curT[0]), max(b, curT[1]), max(c, curT[2])]
        if curT == target:
            return True
        print(curT)
        return False
        