class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = set()
        row = set()

        for i in range(9):
            column.clear()
            row.clear()
            for j in range(9):
                if board[i][j] in column and board[i][j] != ".":
                    return False
                else:
                    column.add(board[i][j])

                if board[j][i] in row and board[j][i] != ".":
                    return False
                else:
                    row.add(board[j][i])
        
        block = set()
        for l in range(0, 9, 3):
            for i in range(0, 9, 3):
                block.clear()
                for j in range(3):
                    for k in range(3):
                        if board[i + j][k + l] in block and board[i + j][k + l] != ".":
                            return False
                        else:
                            block.add(board[i + j][k + l])
        return True

