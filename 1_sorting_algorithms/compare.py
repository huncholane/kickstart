import random
import time
from bubblesort import bubble_sort
from countingsort import countingsort
from heapsort import heapsort
from insertionsort import insertion_sort
from lumoto_quicksort import lumoto_quicksort
from mergesort import mergesort
from hoare_quicksort import hoare_quicksort
from selectionsort import selection_sort


def timsort(arr):
    arr.sort()
    return arr


algos = [
    # bubble_sort,
    # selection_sort,
    # insertion_sort,
    # mergesort,
    # lumoto_quicksort,
    # hoare_quicksort,
    # heapsort,
    timsort,
    # insertion_sort,
    countingsort,
]


n = 50000
base_arr = [random.randint(0, 100) for i in range(n)]

for algo in algos:
    arr = base_arr.copy()
    start = time.time()
    algo(arr)
    print(f"{algo.__name__}: {time.time()-start:.7f} seconds")
