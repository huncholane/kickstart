import random
import time
from utils import swap


def heapify_up(arr, i):
    if i == 1:
        return
    parent = int(i / 2)
    if arr[parent] < arr[i]:
        swap(arr, i, parent)
        heapify_up(arr, parent)


def heapify_down(arr, start, end):
    # Leaf node
    c1 = (start + 1) * 2 - 1
    c2 = c1 + 1
    if c1 > end:
        return
    # Internal node worker
    if c1 == end or arr[c1] > arr[c2]:
        child = c1
    else:
        child = c2
    if arr[child] > arr[start]:
        swap(arr, start, child)
        heapify_down(arr, child, end)


def build_maxheap(arr):
    for i in range(int(len(arr) / 2), -1, -1):
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
