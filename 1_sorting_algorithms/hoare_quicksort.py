import random
import time

from utils import swap

"""
Hoare Partition Scheme
Hoare partition scheme uses two pointers —  start and end. “start” is assigned the leftmost index, and “end” is assigned the rightmost index of the current partition. Both pointers move towards each other until a wrong pair is encountered. By a wrong pair, we mean:

A pair consisting of an element greater than or equal to pivot at the first pointer …
… and an element smaller than or equal to pivot at the second pointer
The elements of the wrong pair are then swapped. This continues until “start” and “end” meet each other.

In the Hoare partition scheme, you can choose any element of the array as the pivot. But selecting the last element as the pivot is mostly avoided because it may lead to infinite recursion. For example, if the given array is {2, 9, 6, 11} and pivot is arr[end], then the returned index will always be equal to end, and a call to the same quickSort method will be made infinite times.

Note: In this scheme, the pivot’s final location is not necessarily at the returned index, and the subsequent two partitions that the quickSort recurs on are (start to Pi) and (Pi+1 to end) as opposed to (start to Pi-1) and (Pi+1 to end hi) as in Lomuto’s scheme.


algorithm quicksort(A, start, end) is
    if start < end then
        Pi = partition(A, start, end)
        quicksort(A, start, pi)
        quicksort(A, pi + 1, end)
        
algorithm partition(A, start, end) is
    pivot := A[ floor((start + end) / 2) ]
    i = start - 1
    j = end + 1
    Start loop 
        do
            i = i + 1
            while A[i] < pivot            
        do               
            j = j - 1                 
            while A[j] > pivot
        if i ≥ j then
            return j
        swap A[i] with A[j]
"""


def partition(arr, l, r):
    pivot = arr[random.randint(l, r - 1)]
    i, j = l - 1, r + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def helper(arr, l: int, r: int):
    # Leaf node
    if l >= r:
        return
    # Internal node worker
    pi = partition(arr, l, r)
    helper(arr, l, pi)
    helper(arr, pi + 1, r)


def hoare_quicksort(arr):
    """Generally O(nlogn) if the partition is random"""
    helper(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    n = 5
    arr = [random.randint(0, n) for i in range(n)]
    print(arr)

    start = time.time()
    hoare_quicksort(arr)
    print(time.time() - start, "seconds")
    print(arr[:5])
