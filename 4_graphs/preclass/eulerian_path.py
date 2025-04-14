def has_eulerian_path(n, edges):
    degrees = [0] * n
    for e in edges:
        degrees[e[0]] += 1
        degrees[e[1]] += 1
    num_odd = 0
    for d in degrees:
        if d % 2 == 1:
            num_odd += 1
    return num_odd == 0 or num_odd == 2


result = has_eulerian_path(
    **{"n": 4, "edges": [[0, 1], [1, 2], [1, 3], [2, 0], [3, 2]]}
)
print(result)
