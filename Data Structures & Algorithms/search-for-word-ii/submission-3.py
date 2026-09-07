class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False 

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = []
        resSet = set()
        tree = PrefixTree()

        for word in words:
            tree.insert(word)
        
        def backtrack(x, y, cur, word, seen):
            if cur.endOfWord:
                if word not in resSet:
                    resSet.add(word)
                    res.append(word)
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] in cur.children and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    backtrack(nx, ny, cur.children[board[nx][ny]], word + board[nx][ny], seen)
                    seen.remove((nx, ny))

        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                if char in tree.root.children:
                    initial_node = tree.root.children[char]
                    initial_word = char 
                    seen = set([(i, j)])
                    backtrack(i, j, initial_node, initial_word, seen)
        return res

