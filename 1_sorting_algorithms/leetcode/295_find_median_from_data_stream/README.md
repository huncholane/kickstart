# [295. Find Median From Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

## Requirements

- Maintain the median after each insert

## Solution 1 - Min and Max Heap

- Intialize with a min heap and a max heap (-min heap)
- Update the heaps on each add making sure they stay within a difference of 1 or 0
- Add to minheap when the value is greater than the smallest item on the minheap
- Swap the middle values when they get too far apart
- Return the minheap root or the maxheap root if one has more items
- Return the median of the roots if they have the same length
