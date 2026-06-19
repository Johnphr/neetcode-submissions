class PrefixTree:

    def __init__(self):
        self.words = set()

    def insert(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        l = len(prefix)
        for word in self.words:
            if word[0:l] == prefix:
                return True
        return False