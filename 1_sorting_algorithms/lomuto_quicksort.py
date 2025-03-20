import random
import time
from traceback import format_exc

from test import test_sorting

"""
Lomuto Partition Scheme
Lomuto partition scheme selects a pivot element, which is typically the last element of the array. While partitioning a range [start, end], the algorithm maintains index i as it scans the array.

Necessary swaps are made to ensure that after every iteration:

The elements from index “start” to i-1 (inclusive) contain the numbers smaller than the pivot
The elements from index i through the last scanned number (inclusive) are equal to or larger than the pivot

algorithm quicksort(A, start, end) is
    if start < end then
        pi = partition(A, start, end)
        quicksort(A, start, pi - 1)
        quicksort(A, pi + 1, end)

algorithm partition(A, start, end) is
    pivot = A[end]
    i = start - 1
    for j = start to end do
        if A[j] < pivot then
        i = i + 1
        swap A[i] with A[j]
    swap A[i+1] with A[end]
    return i+1
"""


def partition(arr, l, r):
    i = l
    for j in range(l + 1, r + 1):
        if arr[j] < arr[l]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[i] = arr[i], arr[l]
    return i


def helper(arr, l, r):
    if l >= r:
        return
    pi = partition(arr, l, r)
    helper(arr, l, pi - 1)
    helper(arr, pi + 1, r)


def lomuto_quicksort(arr):
    helper(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    n = 10
    arr = [random.randint(0, n) for i in range(n)]
    print(arr)

    start = time.time()
    lomuto_quicksort(arr)
    print(time.time() - start, "seconds")
    try:
        test_sorting(lomuto_quicksort, 100, 100)
        print(f"\033[32mGreat success!\033[0m")
    except Exception as e:
        print(f"\033[31mSomething horrible happened: {e}\033[0m")
        print(format_exc())
