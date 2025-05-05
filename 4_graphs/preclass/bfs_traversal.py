def bfs_traversal(n, edges):
    adj_list = [[] for _ in range(n)]
    for e in edges:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])
    visited = [False] * n
    parent = [None] * n
    captured = []
    cc = []
    cross_edges = []
    for i in range(n):
        if not visited[i]:
            cc.append([])
            q = [i]
            visited[i] = True
            while q:
                v = q.pop(0)
                captured.append(v)
                cc[-1].append(v)
                for w in adj_list[v]:
                    if not visited[w]:
                        parent[w] = v
                        q.append(w)
                        visited[w] = True
                    elif parent[v] != w and parent[v] is not None:
                        cross_edges.append([w, v])
    return captured, cc, cross_edges


captured, connected_captures, cross_edges = bfs_traversal(
    **{"n": 6, "edges": [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]}
)
print("All Captured", captured)
print("Connected Captures")
for cc in connected_captures:
    print(cc)
print("Cross Edges")
for ce in cross_edges:
    print(ce)
