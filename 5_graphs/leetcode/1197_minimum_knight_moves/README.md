# [1197. Minimum Knight Moves](https://leetcode.com/problems/minimum-knight-moves/)

## Requirements

- Find the minimum moves it takes to get to position x,y

## BFS Solution

- Make a get adjacency function
- Use a hashmap for visited. Use coordinates as tuples for key and distance for value.
- Perform bfs
- Update distance based on the source distance + 1
- Return once the captured node is the target
