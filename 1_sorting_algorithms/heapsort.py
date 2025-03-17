import random
import time
from utils import swap


def heapify_down(arr, root_index, end):
    # Leaf node
    c1 = (root_index + 1) * 2 - 1
    c2 = c1 + 1
    if c1 > end:
        return
    # Internal node worker
    if c1 == end or arr[c1] > arr[c2]:
        child = c1
    else:
        child = c2
    if arr[child] > arr[root_index]:
        swap(arr, root_index, child)
        heapify_down(arr, child, end)


def build_maxheap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(arr, i, len(arr) - 1)


def extract(arr, end):
    result = arr[end]
    swap(arr, 0, end)
    heapify_down(arr, 0, end - 1)
    # heapify_up(arr, end-1)
    return result


def heapsort(arr):
    build_maxheap(arr)
    for i in range(len(arr) - 1, -1, -1):
        extract(arr, i)
    return arr


if __name__ == "__main__":
    n = 5
    arr = [random.randint(0, n) for i in range(n)]

    start = time.time()
    heapsort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
