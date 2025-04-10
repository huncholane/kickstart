# Graphs

[Leet Code Questions](./leetcode)

## Time Complexities

- DFS and BFS on adjacency lists are O(m+n)

## Definitions

- **DAG**: Directed acyclic graph, typically used for topological sort. Acyclic just means no cycles in the graph.
- **Adjacency Map**: Stores a list/map of maps with `vertex:edge_weight` for each vertex. For example `0 -> {1: 10}` means vertex 0 is connected to vertex 1 with a weight of 10.
