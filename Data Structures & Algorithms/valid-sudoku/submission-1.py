class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Create a set of the valid nums
        nums = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

        # 2. Create a list of sets for the rows, the columns and the blocks
        rows = [set() for _ in range(9)] 
        columns = [set() for _ in range(9)] 
        blocks = [[set() for i in range(3)] for _ in range(3)]

        # 3. Iterate and make sure its valid
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in nums:
                    n = board[i][j] 
                    if n in rows[i] or n in columns[j] or n in blocks[i // 3][j // 3]:
                        # print(n, i, j, rows, columns, blocks)
                        return False
                    rows[i].add(n)
                    columns[j].add(n)
                    blocks[i // 3][j // 3].add(n)

        return True
