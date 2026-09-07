import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []
        heapq.heapify(self.small)
        heapq.heapify(self.big)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.big, num)
        if len(self.big) > len(self.small):
            heapq.heappush(self.small, heapq.heappop(self.big) * -1)
        else:
            if self.small[0] * -1 > self.big[0]:
                temp1 = heapq.heappop(self.small) * -1
                temp2 = heapq.heappop(self.big) * -1
                heapq.heappush(self.small, temp2)
                heapq.heappush(self.big, temp1)

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return self.small[0] * -1
        return (self.small[0] * -1 + self.big[0]) / 2
        