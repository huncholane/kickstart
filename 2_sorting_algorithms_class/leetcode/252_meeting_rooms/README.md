# [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)

## Requiremnts

- Make sure the meetings never overlap

## Presort Solution

- Return true if less than 2 intervals
- Sort the intervals based on start O(nlogn)
- Loop through the intervals and make sure the start is after the previous end O(n)
