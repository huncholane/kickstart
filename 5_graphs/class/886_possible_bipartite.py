from typing import List


class Solution:
    """DFS Solution, check for even/odd cycle using color method"""

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n + 1)]
        for e in dislikes:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
        visited = [False] * (n + 1)
        parent = [None] * (n + 1)
        color = [False] * (n + 1)

        def dfs(s):
            visited[s] = True
            for w in adj_list[s]:
                if not visited[w]:
                    parent[w] = s
                    color[w] = not color[s]
                    if not dfs(w):
                        return False
                elif parent[s] != w and color[s] == color[w]:
                    return False
            return True

        for i in range(1, n + 1):
            if not visited[i]:
                if not dfs(i):
                    return False
        return True
