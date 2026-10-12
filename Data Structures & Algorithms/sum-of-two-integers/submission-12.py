class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        ogA = a
        ogB = b
        a &= mask
        b &= mask
        res = 0
        lol = False
        c = 0
        while a != 0 or b != 0:
            #print(a, b)
            aR = a & 1
            bR = b & 1
            
            a >>= 1
            b >>= 1
            temp = aR ^ bR
            #print(aR, bR, temp)
            if lol:
                if temp == 0:
                    temp = 1
                else:
                    temp = 0
                if aR == 0 and bR == 0:
                    lol = False
            temp <<= c
            res |= temp
            if aR == 1 and bR == 1:
                lol = True
            #print(bin(res), temp, lol)
            c += 1
        #print(lol)
        
        if lol and ((ogA > 0 and ogB > 0)):
            temp = 1
            temp <<= c
            res |= temp
        res &= mask
        if res > 0x7FFFFFFF:
            return ~(res ^ mask)
        return res