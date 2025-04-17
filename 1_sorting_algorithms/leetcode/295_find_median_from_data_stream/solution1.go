package solutions

import "container/heap"

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(val any)      { *h = append(*h, val.(int)) }
func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type MedianFinder struct {
	minheap *IntHeap
	maxheap *IntHeap
}

func (m MedianFinder) Leftn() int      { return m.maxheap.Len() }
func (m MedianFinder) Rightn() int     { return m.minheap.Len() }
func (m MedianFinder) Leftv() float64  { return -float64((*m.maxheap)[0]) }
func (m MedianFinder) Rightv() float64 { return float64((*m.minheap)[0]) }

func Constructor() MedianFinder {
	minheap := &IntHeap{}
	maxheap := &IntHeap{}
	heap.Init(minheap)
	heap.Init(maxheap)
	return MedianFinder{minheap, maxheap}
}

func (this *MedianFinder) AddNum(num int) {
	if this.Rightn() == 0 || float64(num) > this.Rightv() {
		heap.Push(this.minheap, num)
	} else {
		heap.Push(this.maxheap, -num)
	}
	if this.Rightn() > this.Leftn()+1 {
		heap.Push(this.maxheap, -heap.Pop(this.minheap).(int))
	} else if this.Leftn() > this.Rightn()+1 {
		heap.Push(this.minheap, -heap.Pop(this.maxheap).(int))
	}
}

func (this *MedianFinder) FindMedian() float64 {
	if this.Leftn() > this.Rightn() {
		return this.Leftv()
	} else if this.Rightn() > this.Leftn() {
		return this.Rightv()
	} else if this.minheap.Len() == 0 && this.maxheap.Len() == 0 {
		return 0
	} else {
		return (this.Leftv() + this.Rightv()) / 2
	}
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */
