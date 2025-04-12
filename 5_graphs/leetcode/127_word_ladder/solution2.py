from typing import List
from collections import deque
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Create word set and bail early if not possible
        words = set(wordList)
        words.add(beginWord)
        if endWord not in wordList:
            return 0

        # Initialize bfs distance and queue
        m = len(beginWord)
        distance = {beginWord: 1}
        q = deque([beginWord])
        words.remove(beginWord)

        # Run bfs by changing one char at a time for each char in [0,m-1]
        while q:
            w = q.popleft()
            if w == endWord:
                return distance[w]
            for c in string.ascii_lowercase:
                for i in range(m):
                    word = w[:i] + c + w[i + 1 :]
                    if word in words:
                        words.remove(word)
                        q.append(word)
                        distance[word] = distance[w] + 1
        return 0
