# [997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)

## Requirements

- Find the town judge
- The town judge trusts nobody
- Everyone except the town judge trusts the town judge
- Find the one that trusts nobody and is trusted by all

## Degree Solution

- Use artificial 1 based indexing
- Get the indegree and outdegree for each person
- Find the max val in indegree array
- If the max indegree == n-1, There is a potential judge
- Check that the candidate trusts nobody
