class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        def backtrack(curG, queens, cols, diag, anti):
            nonlocal n
            nonlocal res
            for i in range(n):
                # Checks
                if (i not in cols) and (i + (n - queens) not in diag) and ((n - queens) - i not in anti):
                        cols.add(i)
                        anti.add((n - queens) - i)
                        diag.add(i + (n - queens))
                        # Queen is placed
                        curG[(n - queens)][i] = 'Q'
                        queens -= 1

                        # Exit Condition
                        if queens == 0:
                            res.append([''.join(row) for row in curG])
                            print(res)
                        else:
                            backtrack(curG, queens, cols, diag, anti)
                        
                        # Undos
                        queens += 1
                        curG[(n - queens)][i] = '.'
                        cols.remove(i)
                        anti.remove((n - queens) - i)
                        diag.remove(i + (n - queens))

        backtrack(grid, n, set(), set(), set())
        return res