import random
import time

from yaspin import yaspin
from yaspin.spinners import Spinners
from bubblesort import bubble_sort
from countingsort import countingsort
from heapsort import heapsort
from insertionsort import insertion_sort
from lomuto_quicksort import lomuto_quicksort
from mergesort import mergesort
from hoare_quicksort import hoare_quicksort
from radixsort import radixsort
from selectionsort import selection_sort
from quicksort3 import quicksort3
import numpy as np


def timsort(arr):
    arr.sort()
    return arr


algos = [
    # bubble_sort,
    # selection_sort,
    # insertion_sort,
    mergesort,
    # lomuto_quicksort,
    hoare_quicksort,
    quicksort3,
    # heapsort,
    timsort,
    # insertion_sort,
    # countingsort,
    # radixsort,
]


n = 50000
k = 10
with yaspin(Spinners.clock, text="Generating numbers"):
    base_arr = [random.randint(0, k) for i in range(n)]

for algo in algos:
    with yaspin(Spinners.aesthetic, text=f"Running {algo.__name__}") as sp:
        arr = base_arr.copy()
        start = time.time()
        algo(arr)
    print(f"{algo.__name__}: {time.time()-start:.7f} seconds")
