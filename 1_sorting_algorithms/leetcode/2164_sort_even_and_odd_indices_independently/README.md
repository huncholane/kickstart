# [2164. Sort Even and Odd Indices Independently](https://leetcode.com/problems/sort-even-and-odd-indices-independently/) ✅

## Requirements

- Sort even indices increasing and odd indices decreasing

## Solution 1

- Gather even and odd indices into two arrays
  - O(n)
- Sort evens increasing
  - O(nlogn)
- Sort odds decreasing
  - O(nlogn)
- Merge into result
  - t O(n)

## Solution 2 - Heaps

- Store even numbers into a min heap and odd numbers into a max heap (negative minheap)
  - O(nlogn)
- Replace each value in the original array by popping even and odd while incrementing after each pop
  - O(nlogn)
