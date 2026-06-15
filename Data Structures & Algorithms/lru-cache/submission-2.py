class LRUCache:

    def __init__(self, capacity: int):
        self.myDict = {}
        self.keys = []
        self.maxCapacity = capacity

    def get(self, key: int) -> int:
        if key in self.myDict:
            self.keys.append(key)
            self.keys.pop(self.keys.index(key))
            return self.myDict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.keys.append(key)
        if key in self.myDict:
            self.keys.pop(self.keys.index(key))
        self.myDict[key] = value
        if len(self.keys) > self.maxCapacity:
            keyToPop = self.keys.pop(0)
            self.myDict.pop(keyToPop)
            print(self.myDict)