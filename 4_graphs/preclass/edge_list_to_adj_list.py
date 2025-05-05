def edge_list_to_adj_list(n, edges):
    adj_list = [[] for _ in range(n)]
    for e in edges:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])
    return adj_list


result = edge_list_to_adj_list(
    **{"n": 5, "edges": [[0, 1], [1, 4], [1, 2], [1, 3], [3, 4]]}
)
for l in result:
    print(l)
