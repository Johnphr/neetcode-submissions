class Solution:
    def checkPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        def backtrack(i, w):
            if len(w) <= 0:
                test = True
                for el in subset:
                    if test:
                        test = self.checkPalindrome(el)
                if test:
                    res.append(subset.copy())
                return
            subset.append(s[len(s)-len(w)])
            backtrack(i, w[i+1:len(w)])
            subset.pop()
            if subset:
                subset[len(subset) - 1] += w[0]
                backtrack(i, w[i+1:len(w)])
            
        backtrack(0, s)
        return res
