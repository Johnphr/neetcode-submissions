import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            if stone1 != stone2:
                heapq.heappush(max_heap, -abs(stone1 - stone2))
        if not max_heap:
            return 0
        return -max_heap[0]