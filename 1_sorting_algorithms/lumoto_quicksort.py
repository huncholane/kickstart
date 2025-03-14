import random
import time

from utils import swap


def helper(arr, start, end):
    # Leaf node
    if start >= end:
        return
    # Internal node worker
    pivotindex = random.randint(start, end)
    swap(arr, start, pivotindex)
    smaller = start
    for bigger in range(start + 1, end + 1):
        if arr[bigger] < arr[start]:
            smaller += 1
            swap(arr, bigger, smaller)
    swap(arr, start, smaller)
    helper(arr, start, smaller - 1)
    helper(arr, smaller + 1, end)


def lumoto_quicksort(arr):
    """O(nlogn) very fast but requires extra memory"""
    helper(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    n = 5
    arr = [random.randint(0, n) for i in range(n)]

    start = time.time()
    lumoto_quicksort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
