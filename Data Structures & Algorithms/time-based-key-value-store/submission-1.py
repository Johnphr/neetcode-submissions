class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = {}
        self.keys[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        r = len(self.keys[key]) - 1
        l = 0
        en_dict = list(enumerate(self.keys[key].items()))
        most_recent = 0
        while l <= r:
            m = (l + r) // 2
            if en_dict[m][1][0] == timestamp:
                return en_dict[m][1][1]
            elif en_dict[m][1][0] > timestamp:
                r = m - 1
            else:
                l = m + 1
                most_recent = max(most_recent, en_dict[m][1][0])
        if most_recent > 0:
            return self.keys[key][most_recent]
        return ""
