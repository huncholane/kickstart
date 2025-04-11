from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False] * len(graph)
        parent = [None] * len(graph)
        distance = [None] * len(graph)

        def bfs(s):  # is the connected component bipartite
            visited[s] = True
            q = [s]
            distance[s] = 0
            while q:
                v = q.pop(0)
                for w in graph[v]:
                    if not visited[w]:
                        visited[w] = True
                        parent[w] = v
                        distance[w] = distance[v] + 1
                        q.append(w)
                    elif w != parent[v]:
                        if distance[w] == distance[v]:
                            return False  # same level cross edge makes odd length cycle
            return True  # bipartite

        for i in range(len(graph)):
            if not visited[i]:
                if not bfs(i):
                    return False
        return True


class Solution:
    """DFS Solution checks back edges are make an even cycle or not"""

    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False] * len(graph)
        parent = [None] * len(graph)
        color = [False] * len(graph)

        def dfs(s):  # is bipartite
            visited[s] = True
            for w in graph[s]:
                if not visited[w]:
                    parent[w] = s
                    color[w] = not color[s]  # color should be opposite of parent
                    if not dfs(w):
                        return False
                elif (
                    parent[s] != parent[w] and color[w] == color[s]
                ):  # bipartite if parent has opposite color in a cycle
                    return False
            return True

        for i in range(len(graph)):
            if not visited[i]:
                if not dfs(i):
                    return False
        return True
