from typing import List


class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
        visited = [False] * n
        parent = [None] * n

        def bfs(s):
            # Search for cycle
            visited[s] = True
            q = [s]
            while q:
                v = q.pop(0)
                for w in adj_list[v]:
                    if not visited[w]:
                        parent[w] = v
                        visited[w] = True
                        q.append(w)
                    elif parent[v] != w:
                        print(parent[v], w, v)
                        return True
            return False

        for i in range(n):
            if not visited[i]:
                if i > 0:
                    return False
                if bfs(i):  # found a cycle
                    return False
        return True


class Solution:
    """Recursive DFS solution, check for back edges"""

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
        visited = [False] * n
        parent = [None] * n

        def dfs(s):
            visited[s] = True
            for w in adj_list[s]:
                if not visited[w]:
                    parent[w] = s
                    if dfs(w):
                        return True
                elif parent[s] != w:
                    return True
            return False

        for i in range(n):
            if not visited[i]:
                if i > 0:
                    return False
                if dfs(i):  # found a cycle
                    return False
        return True
