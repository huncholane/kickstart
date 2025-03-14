import random
import time
from bubblesort import bubble_sort
from heapsort import heapsort
from insertionsort import insertion_sort
from lumoto_quicksort import lumoto_quicksort
from mergesort import mergesort
from hoare_quicksort import hoare_quicksort
from selectionsort import selection_sort


algos = [
    # bubble_sort,
    # selection_sort,
    # insertion_sort,
    mergesort,
    lumoto_quicksort,
    hoare_quicksort,
    heapsort,
]


n = 50000
base_arr = [random.randint(0, n) for i in range(n)]

for algo in algos:
    arr = base_arr.copy()
    start = time.time()
    algo(arr)
    print(f"{algo.__name__}: {time.time()-start:.4f} seconds")
