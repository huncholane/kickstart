package solutions

import (
	"container/heap"
	"fmt"
	"math"
	"sort"
)

type CarHeap [][]int

func (h CarHeap) Len() int           { return len(h) }
func (h CarHeap) Less(i, j int) bool { return h[i][2] < h[j][2] }
func (h CarHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h CarHeap) Passengers() int {
	res := 0
	for _, info := range h {
		res += info[0]
	}
	return res
}
func (h CarHeap) PeekEnd() int  { return h[0][2] }
func (h *CarHeap) Push(val any) { *h = append(*h, val.([]int)) }
func (h *CarHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func carPooling(trips [][]int, capacity int) bool {
	sort.Slice(trips, func(i, j int) bool {
		return trips[i][1] < trips[j][1]
	})

	h := &CarHeap{}
	heap.Init(h)

	n := len(trips)
	for i := range n {
		var nextstart int
		if i == n-1 {
			nextstart = math.MaxInt
		} else {
			nextstart = trips[i+1][1]
		}
		heap.Push(h, trips[i])
		fmt.Println(h.Passengers())
		if h.Passengers() > capacity {
			return false
		}
		for h.Len() > 0 && h.PeekEnd() <= nextstart {
			heap.Pop(h)
		}
	}
	return true
}
