package solutions

import "container/heap"

type FreqHeap struct {
	H    []int
	freq map[int]int
}

func (h FreqHeap) Len() int           { return len(h.H) }
func (h FreqHeap) Less(i, j int) bool { return h.freq[h.H[i]] < h.freq[h.H[j]] }
func (h FreqHeap) Swap(i, j int)      { h.H[i], h.H[j] = h.H[j], h.H[i] }
func (h *FreqHeap) Push(val any)      { h.H = append(h.H, val.(int)) }
func (h *FreqHeap) Pop() any {
	old := h.H
	n := len(old)
	x := old[n-1]
	h.H = old[:n-1]
	return x
}

func topKFrequent(nums []int, k int) []int {
	freq := make(map[int]int)

	h := &FreqHeap{H: make([]int, 0, k), freq: freq}
	heap.Init(h)
	for _, e := range nums {
		freq[e] += 1
	}
	for key, _ := range freq {
		heap.Push(h, key)
		if h.Len() > k {
			heap.Pop(h)
		}
	}
	return h.H
}
