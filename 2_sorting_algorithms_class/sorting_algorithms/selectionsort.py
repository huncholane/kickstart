import random
import time

from utils import swap


def selection_sort(arr):
    """O(n2) less swaps than bubble sort but still bad"""
    for i in range(len(arr)):
        minval = arr[i]
        minind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < minval:
                minval = arr[j]
                minind = j
        swap(arr, minind, i)
    return arr


if __name__ == "__main__":
    n = 50000
    arr = [random.randint(0, n) for i in range(n)]

    start = time.time()
    selection_sort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
