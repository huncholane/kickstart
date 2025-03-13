import random
import time
from bubblesort import bubble_sort
from insertionsort import insertion_sort
from mergesort import mergesort
from selectionsort import selection_sort


algos = [
    # bubble_sort,
    # selection_sort,
    # insertion_sort,
    mergesort,
]


n = 50000
base_arr = [random.randint(0, n) for i in range(n)]

for algo in algos:
    arr = base_arr.copy()
    start = time.time()
    algo(arr)
    print(f"{algo.__name__}: {time.time()-start:.4f} seconds")
