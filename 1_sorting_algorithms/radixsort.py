import math
import random
import time


"""
Asymptotic complexity in terms of size of array `n`, maximum digits in an element `d`:
* Time: O(n * d).
* Auxiliary space: O(n).
* Total space: O(n).
"""


def counting_sort(arr, place):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements.
    for i in range(0, size):
        index = arr[i] // place
        count[index % 10] += 1

    # Calculate cumulative count.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order.
    i = size - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]


def radixsort(arr):
    # Get maximum element
    max_element = max(arr)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        counting_sort(arr, place)
        place *= 10

    return arr


if __name__ == "__main__":
    n = 5
    arr = [random.randint(0, 300) for i in range(n)]
    print(arr, "\n")

    start = time.time()
    radixsort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
