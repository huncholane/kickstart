# [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

## Requirements

- Return ordering of courses if possible

## DFS Solution

- Make sure there is no cycle using DFS back edges
- Utilize array called topsort
- Topsort keeps list of first departed to last departed
- The reversed topsort gives the list in the correct order

## Kahn Solution

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
- Return the topsort list if there are no cycles
- Khan is an alternate solution for cycle detection
