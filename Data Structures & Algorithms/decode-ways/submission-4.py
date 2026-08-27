class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        invalid = set(['0', '7', '8', '9'])
        starts = set(['1', '2'])
        def dp(s):
            if s in memo:
                return memo[s]
            if len(s) > 0 and s[0] == '0':
                return 0
            if len(s) <= 1:
                return 1
            if len(s) > 1 and ((s[0] == '1' and s[1] != '0') or (s[0] == '2' and s[1] not in invalid)):
                memo[s] = dp(s[1:len(s)]) + dp(s[2:len(s)])
            elif len(s) > 1 and (s[0] in starts and s[1] == "0"):
                memo[s] = dp(s[2:len(s)])
            else:
                memo[s] = dp(s[1:len(s)])
            return memo[s]
        return dp(s)