package solutions

import (
    "container/heap"
)

type IntHeap []int

func (h IntHeap) Len() int {return len(h)}
func (h IntHeap) Less(i,j int) bool {return h[i]<h[j]}
func (h IntHeap) Swap(i,j int) {h[i],h[j]=h[j],h[i]}

func (h *IntHeap) Push(x any) {*h=append(*h,x.(int))}
func (h *IntHeap) Pop() any {
    old:=*h
    n:=len(old)
    x:=old[n-1]
    *h=old[:n-1]
    return x
}

type KthLargest struct {
    H IntHeap
    K int
}


func Constructor(k int, nums []int) KthLargest {
    kl:=KthLargest{
        H: IntHeap{},
        K: k,
    }
    for _,num:=range nums {
        kl.Add(num)
    }
    return kl
}


func (this *KthLargest) Add(val int) int {
    heap.Push(&this.H,val)
    if len(this.H)>this.K {
        heap.Pop(&this.H)
    }
    return this.H[0]
}


/**
 * Your KthLargest object will be instantiated and called as such:
 * obj := Constructor(k, nums);
 * param_1 := obj.Add(val);
 */