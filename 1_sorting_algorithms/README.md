# Sorting Algorithms

## [LeetCode Problems](./leetcode)

## Partitioning Algorithms

- Lomuto (increasing order)
  - Left to right (or right to left)
  - Pick a random index in range [left,right] and swap with the left index
  - Use the left index as a pivot
  - Use a fast pointer and a slow pointer
  - Whenever the fast pointer is less than the pivot, swap fast and slow values in place
  - Swap left value with slow value to get the pivot in the right place
  - Return the slow pointer since this is the pivot index
- Hoare (increasing order)
  - Pick a random index in range [left,right), right is avoided to prevent infinite recursion
  - Use the value at the random index for the pivot
  - Use a pointer to the left and right
  - Loop
    - Slide left to the right until a value is larger than the pivot
    - Slide right to left until a value is smaller than the pivot
    - Return right index if the left pointer has moved past the right index
    - Swap the right and left
- 3 Way Partition (increasing order)
  - Creates a partitioning wall to fight against repeated numbers

```
Pick random pivot
Two left pointers and one right pointer
While mid index is less than right index
  If mid val is smaller than the pivot
    Swap left and mid
    Increment left index and mid index
  If mid val is equal to the pivot
    Increment mid index
  If mid val is larger than the pivot
    Swap mid and right
    Decrement right index
Return the left and right indexes
```

## Sorting Algorithms

- Quicksort
  - In place
  - Not Stable
  - O(nlogn) on average
  - O(n2) if all the elements are already sorted (Combat with random pivots)
  - O(n2) if all elements are the same unless using 3 way partition
  - Use a partitioning scheme to select a pivot index and recursively call on [left,pivot-1] and [pivot+1,right]
- Mergesort
  - Uses auxilliary space
  - Stable
  - O(nlogn) gauranteed
