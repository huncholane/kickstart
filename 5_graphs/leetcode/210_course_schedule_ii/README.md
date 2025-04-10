# [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

## Requirements

- Return ordering of courses if possible

## DFS Solution

- Make sure there is no cycle using DFS back edges
- Utilize array called topsort
- Topsort keeps list of first departed to last departed
- The reversed topsort gives the list in the correct order
