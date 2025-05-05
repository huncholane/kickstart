package cancelable

import (
	"context"
	"sortingalgos/internal/utils"
)

func CountingSort(ctx context.Context, arr []int) {
	if len(arr) == 0 {
		return
	}
	low, high := arr[0], arr[0]
	for _, x := range arr {
		if utils.Cancelled(ctx) {
			return
		}
		if x < low {
			low = x
		} else if x > high {
			high = x
		}
	}

	k := high - low + 1
	counts := make([]int, k)
	for _, x := range arr {
		if utils.Cancelled(ctx) {
			return
		}
		counts[x-low]++
	}

	i := 0
	for v, c := range counts {
		if utils.Cancelled(ctx) {
			return
		}
		for j := 0; j < c; j++ {
			arr[i] = v + low
			i++
		}
	}
}
