class Solution:
    def isPalindrome(self, s: str) -> bool:
        pL = 0
        pR = len(s) - 1
        if len(s) == 1:
            return True
        while pL < pR:
            if not(65 <= ord(s[pL].upper()) <= 90) and not(48 <= ord(s[pL].upper()) <= 57):
                pL += 1
                continue
            if not(65 <= ord(s[pR].upper()) <= 90) and not(48 <= ord(s[pR].upper()) <= 57):
                pR -= 1
                continue
            if ord(s[pR].upper()) == ord(s[pL].upper()):
                pL += 1
                pR -= 1
            else:
                return False
        return True
        