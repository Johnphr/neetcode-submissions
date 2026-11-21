class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def f_m(m):
            if m == 0:
                return False
            tot = 0
            for pile in piles:
                tot += math.ceil(pile / m)
            if tot <= h:
                return True
            return False

        l = 0
        r = max(piles)
        res = r
        while (r - l >= 0):
            m = l + (r - l) // 2
            val = f_m(m)
            if val:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res