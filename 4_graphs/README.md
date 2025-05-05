# Graphs

[Leet Code Questions](./leetcode)

## Time Complexities

- DFS and BFS on adjacency lists are O(m+n)

## Definitions

- **Graph**: A collection of vertices and edges.
- **Cycle**: A path around a graph that goes back to its original vertex.
- **Eulerian Cycle**: A cycle that covers all vertices of a graph using each edge only once.
- **Eulerian Path**: A path that covers all vertices of a graph starting at one point and reaching another.
- **Connected Components**: Vertices in a graph where every vertex has a path to reach all other vertices.
- **Adjacency Map**: Stores a list/map of maps with `vertex:edge_weight` for each vertex. For example `0 -> {1: 10}` means vertex 0 is connected to vertex 1 with a weight of 10.
- **DAG**: Directed acyclic graph, typically used for topological sort. Acyclic just means no cycles in the graph.
