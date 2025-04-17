# [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) ✅

## Requirements

- Figure out how many meeting rooms are needed for a set of intervals that represent meetings to complete them all

## Solution 1 - Priority Queue (Heap)

- Presort from start time
- Use the template
- Add the end of a meeting to the priority queue (minheap)
- Save result as max
- Remove all the meetings that end before the next meeting
- The number of meetings is always in the priority queue
