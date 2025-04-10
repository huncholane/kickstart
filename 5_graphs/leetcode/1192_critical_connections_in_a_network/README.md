# [1192. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/)

# Requirements

- Find edges the cause multiple servers to become unreachable

# Khan Solution

- O(m+n): Build the graph, topsort=[]
- O(m+n): Find the in-degree of each node
  `(u,v)->in-degree[v]++`
- O(n): Identify nodes that have a zero in-degree and store them into a bag

```
while bag is not empty:
    node = bag.pop()
    // Take that course -> topsort.append(node)
    while bag is not empty:
        for neighbor in adjList[node]:
            in-degree[neighbor]--
            if in-degree[neighbor]==0:
                bag.append(neighbor)
    if size of topsort < n:
        // cycle found
```
