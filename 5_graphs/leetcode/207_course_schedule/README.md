# [207. Course Schedule](https://leetcode.com/problems/course-schedule/description/)

## Requirements

- Make sure all classes are accessible

## DFS Solution

- Convert to directed graph
- Keep track of arrival and departure timestamps, no need for arrival but following template
- Run DFS and ensure there are no cycles (No Back Edges)
