def bfs_traversal(n, edges):
    adj_list = [[] for _ in range(n)]
    for e in edges:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])
    visited = [False] * n
    parent = [None] * n
    captured = []
    for i in range(n):
        if not visited[i]:
            q = [i]
            visited[i] = True
            while q:
                v = q.pop(0)
                captured.append(v)
                for w in adj_list[v]:
                    if not visited[w]:
                        parent[w] = v
                        q.append(w)
                        visited[w] = True
    return captured


captured = bfs_traversal(**{"n": 6, "edges": [[0, 1], [0, 2], [0, 4], [2, 3]]})
print(captured)
