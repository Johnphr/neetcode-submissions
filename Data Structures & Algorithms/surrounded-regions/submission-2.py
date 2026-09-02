from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i,j) not in seen:
                    q = deque([(i, j)])
                    visited_here = set()
                    seen.add((i, j))
                    border = False
                    visited_here.add((i, j))
                    while q:
                        x, y = q.popleft()
                        if x == 0 or x == len(board) - 1 or y == 0 or y == len(board[0]) - 1:
                            border = True
                        for dx, dy in directions:
                            nx = dx + x
                            ny = dy + y
                            if 0 <= nx <= len(board) - 1 and 0 <= ny <= len(board[0]) - 1 and board[nx][ny] == 'O' and (nx, ny) not in seen:
                                seen.add((nx, ny))
                                visited_here.add((nx, ny))
                                q.append((nx, ny))
                    if not border:
                        for x, y in visited_here:
                            board[x][y] = 'X'