# [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

## Requirements

- Merge linked lists

## Solution 1 - Heap

- Create a min heap that stores a tuple of (val,index,node)
  - Make an index that updates in the list traversal for all lists
  - Traverse each list
- Build the list
  - Make a dummy node and pointer
  - Pop the heap until empty and update the pointer
  - Return next from the dummy node
- Can do it in place will try that later
