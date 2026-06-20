class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        l = len(board)
        w = len(board[0])

        def tryg(i, j):
            nonlocal res
            nonlocal c
            nonlocal seen

            if c >= len(word) - 1:
                res = True
                return
            if i < len(board) - 1 and board[i + 1][j] == word[c + 1] and (i + 1, j) not in seen:
                c += 1
                seen.add((i + 1, j))
                tryg(i + 1, j)
                c -= 1
                seen.remove((i + 1, j))
            if i > 0 and board[i - 1][j] == word[c + 1] and (i - 1, j) not in seen:
                c += 1
                seen.add((i - 1, j))
                tryg(i - 1, j)
                c -= 1
                seen.remove((i - 1, j))
            if j < len(board[0]) - 1 and board[i][j + 1] == word[c + 1] and (i, j + 1) not in seen:
                c += 1
                seen.add((i, j + 1))
                tryg(i, j + 1)
                c -= 1
                seen.remove((i, j + 1))
            if j > 0 and board[i][j - 1] == word[c + 1] and (i, j - 1) not in seen:
                c += 1
                seen.add((i, j - 1))
                tryg(i, j - 1)
                c -= 1
                seen.remove((i, j - 1))

        for i in range(l):
            for j in range(w):
                if board[i][j] == word[0]:
                    c = 0
                    seen = set()
                    seen.add((i, j))
                    tryg(i, j)
        
        return res