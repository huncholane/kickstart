package cancelable

import (
	"context"
	"math/rand"
	"sortingalgos/internal/utils"
)

type pair struct {
	l int
	r int
}

// lomutoPartition paritions an array using Lomuto's method with
// the capability to to cancel from the parent
func lomutoPartition(ctx context.Context,arr[]int,l,r int) int {
	pi:=rand.Intn(r-l)+l
	arr[l],arr[pi]=arr[pi],arr[l]
	i:=l
	for j:=l+1;j<=r;j++ {
		if utils.Cancelled(ctx) {return -1}
		if arr[j]<arr[l] {
			i++
			arr[i],arr[j]=arr[j],arr[i]
		}
	}
	arr[l],arr[i]=arr[i],arr[l]
	return i
}

func Lomutosort(ctx context.Context,arr[]int) {
	n:=len(arr)
	stack:=make([]pair,0,n)
	stack=append(stack,pair{l:0,r:n-1})
	for len(stack)>0 {
		n=len(stack)
		p:=stack[n-1]
		stack=stack[:n-1]
		if p.l>=p.r {continue}
		if utils.Cancelled(ctx) {return}
		i:=lomutoPartition(ctx,arr,p.l,p.r)
		if utils.Cancelled(ctx) {return}
		stack=append(stack,pair{l:p.l,r:i-1})
		stack=append(stack,pair{l:i+1,r:p.r})
	}
}

func hoarePartition(ctx context.Context,arr[]int,l,r int) int {
	var pivot int
	if r-l==1 {
		pivot=arr[l]
	} else {
		pivot=arr[rand.Intn(r-l-1)+l]
	}
	i,j:=l-1,r+1
	for {
		if utils.Cancelled(ctx) {return -1}
		i++
		for arr[i]<pivot {
			i++
		}
		if utils.Cancelled(ctx) {return -1}
		j--
		for arr[j]>pivot {
			j--
		}
		if i>=j {
			break
		}
		arr[i],arr[j]=arr[j],arr[i]
	}
	return j
}

func Hoaresort(ctx context.Context,arr[]int) {
	n:=len(arr)
	stack:=make([]pair,0,n)
	stack=append(stack,pair{l:0,r:n-1})
	for len(stack)>0 {
		if utils.Cancelled(ctx) {return}
		n=len(stack)
		p:=stack[n-1]
		stack=stack[:n-1]
		if p.l>=p.r {continue}
		if utils.Cancelled(ctx) {return}
		i:=hoarePartition(ctx,arr,p.l,p.r)
		if utils.Cancelled(ctx) {return}
		stack=append(stack,pair{l:p.l,r:i})
		stack=append(stack,pair{l:i+1,r:p.r})
	}
}

func partition3(ctx context.Context,arr[]int,l,r int) (int,int){
	pivot:=arr[rand.Intn(r-l)+l]
	i,j,k:=l,l,r
	for j<=k {
		if utils.Cancelled(ctx) {return -1,-1}
		if arr[j]<pivot {
			arr[i],arr[j]=arr[j],arr[i]
			i++
			j++
		} else if arr[j]==pivot {
			j++
		} else {
			arr[j],arr[k]=arr[k],arr[j]
			k--
		}
	}
	return i,k
}

func Quicksort3(ctx context.Context,arr[]int) {
	n:=len(arr)
	stack:=make([]pair,0,n)
	stack=append(stack,pair{l:0,r:n-1})
	for len(stack)>0 {
		n=len(stack)
		p:=stack[n-1]
		stack=stack[:n-1]
		if p.l>=p.r {continue}
		if utils.Cancelled(ctx) {return}
		l,r:=partition3(ctx,arr,p.l,p.r)
		if utils.Cancelled(ctx) {return}
		stack=append(stack,pair{l:p.l,r:l-1})
		stack=append(stack,pair{l:r+1,r:p.r})
	}
}