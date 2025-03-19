"""
This function partitions a[] in three parts
   a) a[first..start] contains all elements smaller than pivot
   b) a[start+1..mid-1] contains all occurrences of pivot
   c) a[mid..last] contains all elements greater than pivot

"""

import random
import time
from test import test_sorting


def partition(arr, l, r):
    pivot = arr[l]
    i, j, k = l, l, r
    while j <= k:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] == pivot:
            j += 1
        else:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
    return i, k


def helper(arr, l, r):
    if l >= r:
        return
    if r - l == 1:
        if arr[l] > arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
        return
    pl, pr = partition(arr, l, r)
    helper(arr, l, pl - 1)
    helper(arr, pr + 1, r)


def quicksort3(arr):
    helper(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    n = 5
    k = n
    arr = [random.randint(0, k) for _ in range(n)]
    start = time.time()
    quicksort3(arr)
    print(time.time() - start, "seconds")
    try:
        test_sorting(quicksort3)
        print(f"\033[32mGreat Success\033[0m")
    except Exception as e:
        print(f"Failed: {e}")
