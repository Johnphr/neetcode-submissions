class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        myMap = {}
        for c in s:
            myMap[c] = myMap.get(c, 0) + 1
        mySet = set()
        mySet.add(s[0])
        lastI = 0
        for i in range(len(s)):
            c = s[i]
            if c not in mySet:
                mySet.add(c)
            myMap[c] -= 1
            if myMap[c] == 0:
                mySet.remove(c)
            if not mySet:
                # print(i, lastI)
                res.append(i - lastI + 1)
                lastI = i + 1
        return res
            
        