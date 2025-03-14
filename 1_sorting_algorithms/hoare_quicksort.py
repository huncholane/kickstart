import random
import time

from utils import swap


def helper(arr, start: int, end: int):
    # Leaf node
    if start >= end:
        return
    # Internal node worker
    pivotindex = random.randint(start, end)
    swap(arr, start, pivotindex)
    smaller = start + 1
    bigger = end
    while smaller <= bigger:
        if arr[smaller] < arr[start]:
            smaller += 1
        elif arr[bigger] > arr[start]:
            bigger -= 1
        else:
            swap(arr, smaller, bigger)
            smaller += 1
            bigger -= 1
    swap(arr, bigger, start)
    helper(arr, start, bigger - 1)
    helper(arr, bigger + 1, end)


def hoare_quicksort(arr):
    """O(nlogn) very fast but requires extra memory"""
    helper(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    n = 50000
    arr = [random.randint(0, n) for i in range(n)]

    start = time.time()
    hoare_quicksort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
