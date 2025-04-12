import random
import time

from utils import swap


def bubble_sort(arr):
    """O(n2) most swaps"""
    n = len(arr)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j - 1] > arr[j]:
                swap(arr, j - 1, j)


if __name__ == "__main__":
    n = 50000
    arr = [random.randint(0, n) for i in range(n)]

    start = time.time()
    bubble_sort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
