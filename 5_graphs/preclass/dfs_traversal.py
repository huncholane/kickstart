def dfs_traversal(n, edges):
    adj_list = [[] for _ in range(n)]
    for e in edges:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])
    visited = [False] * n
    captured = []
    parent = [None] * n
    connected_components = []

    def dfs(s):
        visited[s] = True
        captured.append(s)
        connected_components[-1].append(s)
        for w in adj_list[s]:
            if not visited[w]:
                parent[w] = s
                dfs(w)

    for i in range(n):
        if not visited[i]:
            connected_components.append([])
            dfs(i)
    return captured, connected_components


captured, connected_components = dfs_traversal(
    **{"n": 6, "edges": [[0, 1], [0, 2], [1, 4], [3, 5]]}
)

print("Captures", captured)
print("Connected Components")
for cc in connected_components:
    print(cc)
