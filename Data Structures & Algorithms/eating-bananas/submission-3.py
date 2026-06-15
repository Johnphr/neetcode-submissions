class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        k = r
        while l <= r:
            m = (l + r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / m)
            if time > h:
                l = m + 1
            else:
                k = m
                r = m - 1
        return k

        