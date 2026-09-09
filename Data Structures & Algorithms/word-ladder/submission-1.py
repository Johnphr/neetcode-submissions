from collections import deque
class Solution:
    def checkDifferences(self, word1: str, word2: str) -> bool:
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        if diff == 1:
            return True
        return False

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if self.checkDifferences(beginWord, endWord):
            return 2
        
        # 1. Build Graph
        adj = {}
        adj[beginWord] = []
        adj[endWord] = []
        for word in wordList:
            adj[word] = []
            if self.checkDifferences(beginWord, word):
                adj[beginWord].append(word)
                adj[word].append(beginWord)
            if self.checkDifferences(endWord, word):
                adj[endWord].append(word)
                adj[word].append(endWord)
        for i in range(len(wordList)):
            word1 = wordList[i]
            for j in range(i + 1, len(wordList)):
                word2 = wordList[j]
                if self.checkDifferences(word1, word2):
                    adj[word1].append(word2)
                    adj[word2].append(word1)

        print(adj)
        # 2. BFS
        distances = {}
        distances[beginWord] = 1
        q = deque([(1, beginWord)])
        while q:
            dist, node = q.popleft()
            for conn in adj[node]:
                if conn not in distances:
                    distances[conn] = dist + 1
                    q.append((dist + 1, conn))
        if endWord not in distances:
            return 0
        return distances[endWord]
        

