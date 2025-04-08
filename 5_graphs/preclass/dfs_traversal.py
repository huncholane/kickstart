def dfs_traversal(n, edges):
    adj_list = [[] for _ in range(n)]
    for e in edges:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])
    visited = [False] * n
    captured = []
    parent = [None] * n

    def dfs(s):
        visited[s] = True
        captured.append(s)
        for w in adj_list[s]:
            if not visited[w]:
                parent[w] = s
                dfs(w)

    for i in range(n):
        if not visited[i]:
            dfs(i)
    return captured


captured = dfs_traversal(
    **{"n": 8, "edges": [[1, 2], [1, 4], [1, 7], [2, 3], [4, 5], [5, 6]]}
)

print("Captures", captured)
