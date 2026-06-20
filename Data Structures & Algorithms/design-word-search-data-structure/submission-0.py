class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        return self.checkWithDots(cur, word)

    def checkWithDots(self, node: TrieNode, word: str) -> bool:
        cur = node
        for i in range(len(word)):
            if word[i] != '.':
                if word[i] not in cur.children:
                    return False
                cur = cur.children[word[i]]
            else:
                mySet = set()
                for child in cur.children:
                    mySet.add(self.checkWithDots(cur.children[child], word[i + 1: len(word)]))
                if True in mySet:
                    return True
                return False
        return cur.end

            
