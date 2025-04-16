package solutions

import "container/heap"

type IntHeap []int

func (h IntHeap) Len() int {return len(h)}
func (h IntHeap) Less(i,j int) bool {return h[i]<h[j]}
func (h IntHeap) Swap(i,j int) {h[i],h[j]=h[j],h[i]}
func (h *IntHeap) Push(val any) {*h=append(*h,val.(int))}
func (h *IntHeap) Pop() any {
    old:=*h
    n:=len(old)
    x:=old[n-1]
    *h=old[:n-1]
    return x
}

func sortEvenOdd(nums []int) []int {
    n:=len(nums)
    var e IntHeap
    var o IntHeap
    for i,num:=range nums {
        switch {
            case i%2==1:
            heap.Push(&o,-num)
            default:
            heap.Push(&e,num)
        }
    }
    i:=0
    for i<n {
        if len(e)>0{nums[i]=heap.Pop(&e).(int);i++}
        if len(o)>0{nums[i]=-heap.Pop(&o).(int);i++}
    }
    return nums
}