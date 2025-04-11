# [126. Word Ladder](https://leetcode.com/problems/word-ladder/)

## Requirements

- Find the shortest way to transform a word based on a list of words that changes one letter at a time to a word in the list.

## Solution 1 - Using an Adjacency List

- Append the start word to the word list so the bfs can use the last index as the starting point
- Fail early by checking if the end word is even in the list
- Construct undirected graph to represent words that can change into eachother with a difference of one character
- Make visited map to keep track of distance
- Use the last index for the starting point

## Solution 2 - Iterate Characters
