import random
import time


def insertion_sort(arr):
    """Best Case: O(n)
    Average Case: O(n2)
    Worst Case: O(n2)

    Good if you can assume data is almost sorted.
    Shifts instead of swaps."""
    for i in range(0, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


if __name__ == "__main__":
    n = 50000
    arr = [random.randint(0, n) for i in range(n)]

    start = time.time()
    insertion_sort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
