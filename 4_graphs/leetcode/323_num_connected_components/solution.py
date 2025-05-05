from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
        visited = [False] * n

        def bfs(s):
            visited[s] = True
            q = [s]
            while q:
                v = q.pop(0)
                for w in adj_list[v]:
                    if not visited[w]:
                        visited[w] = True
                        q.append(w)

        cc = 0
        for i in range(n):
            if not visited[i]:
                bfs(i)
                cc += 1
        return cc
