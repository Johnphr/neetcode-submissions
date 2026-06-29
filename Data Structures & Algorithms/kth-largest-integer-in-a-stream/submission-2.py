import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.h = nums
        self.k = k

    def add(self, val: int) -> int:
        self.h.append(val)
        self.h.sort()
        return self.h[len(self.h) - self.k]
