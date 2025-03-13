import random
import time
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort


algos = [bubble_sort, insertion_sort, selection_sort]


n = 50000
base_arr = [random.randint(0, n) for i in range(n)]

for algo in algos:
    arr = base_arr.copy()
    start = time.time()
    algo(arr)
    print(f"{algo.__name__}: {time.time()-start:.4f} seconds")
