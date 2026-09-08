class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dp(word):
            if word in memo:
                return memo[word]
            if len(word) <= 0:
                return True
            memo[word] = False
            for w in wordDict:
                if w == word[0:len(w)]:
                    memo[word] = memo[word] or dp(word[len(w):])
            return memo[word]
        return dp(s)