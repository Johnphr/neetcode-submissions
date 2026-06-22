class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        myMap = {'2':['a', 'b', 'c'], 
        '3':['d', 'e', 'f'], 
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'], 
        '8':['t', 'u', 'v'], 
        '9':['w', 'x', 'y', 'z']
        }
        res = []

        def backtrack(s, r):
            nonlocal res
            if len(s) <= 0:
                res.append("".join(r))
                return
            digit = s[0]
            for c in myMap[digit]:
                r.append(c)
                backtrack(s[1:len(s)], r)
                r.pop()
        
        backtrack(digits, [])
        return res
            
        