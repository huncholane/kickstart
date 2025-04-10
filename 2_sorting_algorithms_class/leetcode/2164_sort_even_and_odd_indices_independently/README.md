# [2164. Sort Even and Odd Indices Independently](https://leetcode.com/problems/sort-even-and-odd-indices-independently/) ✅

## Requirements

- Sort even indices increasing and odd indices decreasing

## Solution

1. Gather even and odd indices into two arrays O(n)
2. Sort evens increasing O(nlogn)
3. Sort odds decreasing O(nlogn)
4. Merge into result O(n)
