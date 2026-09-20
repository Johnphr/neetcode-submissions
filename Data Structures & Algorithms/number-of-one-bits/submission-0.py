class Solution:
    def hammingWeight(self, n: int) -> int:
        binrep = bin(n)[2:]
        res = 0
        for num in binrep:
            if num == '1':
                res += 1
        return res