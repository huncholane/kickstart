# [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)

## Requirements

- Get every solution for the word ladder

## Solution 1

- Run bfs and create a DAG in an adjacency map
  - Run inorder bfs and only apply visited at the end of each level
  - Remember bfs from the trees section like how you would print each level of a tree
  - Only add to queue when we haven't added it to the adjacency map yet
  - Always append the word the the parent word's adjacency list
- Run dfs and gather the slates
