# [207. Course Schedule](https://leetcode.com/problems/course-schedule/description/)

## Requirements

- Make sure all classes are accessible

## Solution 1 - DFS

- Convert to directed graph
- Keep track of arrival and departure timestamps, no need for arrival but following template
- Run DFS and ensure there are no cycles (No Back Edges)

## Solution 2 - Kahn

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

- Decrementing in-degree for class c is like taking a prereq for class c
- We prove all classes can be taken if the in-degree for all is 0
- Khan is an alternate solution for cycle detection
