from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        n, m = len(wordList), len(wordList[0])
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                w1, w2 = wordList[i], wordList[j]
                diff = 0
                for k in range(m):
                    if w1[k] != w2[k]:
                        diff += 1
                if diff == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        start = len(wordList) - 1
        visited = {start: 1}
        q = deque([start])
        while q:
            node = q.popleft()
            if wordList[node] == endWord:
                return visited[node]
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited[neighbor] = visited[node] + 1
                    q.append(neighbor)
        return 0
