package solutions

import "container/heap"

type ListNode struct {
	Val  int
	Next *ListNode
}
type NodeHeap []*ListNode

func (h NodeHeap) Len() int           { return len(h) }
func (h NodeHeap) Less(i, j int) bool { return h[i].Val < h[j].Val }
func (h NodeHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *NodeHeap) Push(val any)      { *h = append(*h, val.(*ListNode)) }
func (h *NodeHeap) Pop() any {
	old := *h
	n := len(old)
	node := old[n-1]
	*h = old[:n-1]
	return node
}

func mergeKLists(lists []*ListNode) *ListNode {
	h := &NodeHeap{}

	// Get first K elements O(k)
	for _, node := range lists {
		if node != nil {
			*h = append(*h, node)
		}
	}

	// Init first k elements O(k)
	heap.Init(h)
	dummy := &ListNode{Val: 0, Next: nil}
	tmp := dummy

	// Update the links in the heap nodes O(nlogk)
	for len(*h) > 0 {
		// Pop the heap O(logk)
		node := heap.Pop(h)
		tmp.Next = node.(*ListNode)
		tmp = tmp.Next
		if tmp.Next != nil {
			// Push the heap O(logk)
			heap.Push(h, tmp.Next)
		}
	}

	return dummy.Next
}
