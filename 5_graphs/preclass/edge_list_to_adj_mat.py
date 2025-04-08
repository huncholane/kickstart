def edge_list_to_adj_mat(n, edges):
    adj_mat = [[0 for _ in range(n)] for _ in range(n)]
    for e in edges:
        adj_mat[e[0]][e[1]] = 1
        adj_mat[e[1]][e[0]] = 1
    return adj_mat


result = edge_list_to_adj_mat(
    **{"n": 5, "edges": [[0, 1], [1, 4], [1, 2], [1, 3], [3, 4]]}
)

for l in result:
    print(l)
