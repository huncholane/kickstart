package solutions

import (
	"container/heap"
	"math"
	"sort"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h IntHeap) Peek() int          { return h[0] }
func (h *IntHeap) Push(val any)      { *h = append(*h, val.(int)) }
func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	v := old[n-1]
	*h = old[:n-1]
	return v
}

func minMeetingRooms(intervals [][]int) int {
	// Presort
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	// Set up priority queue
	h := &IntHeap{}
	heap.Init(h)

	res := 0
	n := len(intervals)
	for i := range n {
		var nextstart int
		if i == n-1 {
			nextstart = math.MaxInt
		} else {
			nextstart = intervals[i+1][0]
		}

		// start meeting
		heap.Push(h, intervals[i][1])
		res = max(res, h.Len())

		// end meetings
		for h.Len() > 0 && h.Peek() <= nextstart {
			heap.Pop(h)
		}
	}
	return res
}
