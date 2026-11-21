class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            res = str(x)
            r = int(res[::-1])
            if r < -2 ** 31 or r > 2 ** 31 - 1:
                return 0
            return r
        num = str(x)
        res = num[1:]
        r = int(res[::-1]) * -1
        if r < -2 ** 31 or r > 2 ** 31 - 1:
            return 0
        return r
        