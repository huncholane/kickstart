# [785. Is graph bipartite?](https://leetcode.com/problems/is-graph-bipartite/)

## Requirements

- Find out if graph is bipartite

## Solution

- Construct adjacency list
- Set up visited, parent, and distance maps
- Do a bfs search
- A graph is bipartite if there is a cycle with an odd number of nodes
- We know if a graph is bipartite if there is a cross edge on the same level

```
 odd       even
  o         o
 / \       / \
o---o     o   o
         /   /
        o---/
```

- So, when there is a cross edge whose distance is the same as it's parent, we know there is an odd number of nodes in the cycle
- Run bfs on each connected component and return False if any of them have an odd number of components
