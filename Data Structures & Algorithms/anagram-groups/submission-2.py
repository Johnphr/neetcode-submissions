class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = []
        dicts = {}
        for i in range(len(strs)):
            myDict = {}
            for j in range(len(strs[i])):
                myDict[strs[i][j]] = myDict.get(strs[i][j], 0 ) + 1
            print("I got here")
            myFrozenSet = frozenset(myDict.items())
            if myFrozenSet in dicts:
                dicts[myFrozenSet].append(strs[i])
            else:
                dicts[myFrozenSet] = [strs[i]]

        print("Almost done bro")
        for k, v in dicts.items():
            words.append(v)

        print(words)
        return words