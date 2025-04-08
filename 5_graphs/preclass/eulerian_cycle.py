def has_eulerian_cycle(n, edges):
    degrees = [0] * n
    for e in edges:
        degrees[e[0]] += 1
        degrees[e[1]] += 1
    for degree in degrees:
        if degree % 2 == 1:
            return False
    return True


result = has_eulerian_cycle(
    **{"n": 5, "edges": [[0, 1], [0, 2], [1, 3], [3, 0], [3, 2], [4, 3], [4, 1]]}
)

print(result)
