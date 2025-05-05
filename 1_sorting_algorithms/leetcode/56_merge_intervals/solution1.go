package solutions

import (
	"container/heap"
	"math"
	"sort"
)

type IntervalHeap [][]int

func (h IntervalHeap) Len() int           { return len(h) }
func (h IntervalHeap) Less(i, j int) bool { return h[i][0] < h[j][0] }
func (h IntervalHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h IntervalHeap) Peek() []int        { return h[0] }
func (h *IntervalHeap) Push(val any)      { *h = append(*h, val.([]int)) }
func (h *IntervalHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func merge(intervals [][]int) [][]int {
	n := len(intervals)
	res := make([][]int, 0, n)

	// presort
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	// init the heap
	h := &IntervalHeap{}
	heap.Init(h)

	// interval template
	for i := range n {
		var nextstart int
		if i == n-1 {
			nextstart = math.MaxInt
		} else {
			nextstart = intervals[i+1][0]
		}
		heap.Push(h, intervals[i])
		if h.Len() == 1 {
			// new interval
			res = append(res, intervals[i])
		}
		for h.Len() > 0 && h.Peek()[1] < nextstart {
			res[len(res)-1][1] = max(h.Peek()[1], res[len(res)-1][1])
			heap.Pop(h)
		}
	}
	return res
}
