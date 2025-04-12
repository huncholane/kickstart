from typing import List
from collections import defaultdict, deque


class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if grid[i][j] == 1:
                    adj[i].append(j)

        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
