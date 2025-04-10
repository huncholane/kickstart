# 703. Kth Largest Element in a Stream

## Requirements

- Keep the kth largest element available to extract in constant time.
- Update in O(logk)

## Solution

- Use a min heap initialized to empty.
- Add items to the heap when the size is less than k or the element is larger than the kth largest value.
- Return the smallest item in the heap if the heap has k elements.
