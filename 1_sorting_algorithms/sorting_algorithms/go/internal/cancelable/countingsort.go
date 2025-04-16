package cancelable

import (
	"context"
	"sortingalgos/internal/utils"
)

func CountingSort(ctx context.Context,arr []int) {
	if len(arr)==0 {
		return
	}
	low:=arr[0]
	high:=arr[0]
	n:=len(arr)
	for i:=range n {
		if utils.Cancelled(ctx) {return}
		if arr[i]<low {
			low = arr[i]
		} else if arr[i]>high {
			high=arr[i]
		}
	}

	// make array start from 0
	for i:=range n {
		if utils.Cancelled(ctx) {return}
		arr[i]-=low
	}
	k:=high-low

	// init counts count array
	counts:=make([]int,k+1)
	for i:=range n {
		if utils.Cancelled(ctx) {return}
		counts[arr[i]]+=1
	}

	// cummulate the sums to index correctly
	for i:=1;i<k+1;i++ {
		if utils.Cancelled(ctx) {return}
		counts[i]+=counts[i-1]
	}

	// store output in reverse order and store into original array
	output:=make([]int,n)
	for i:=n-1;i>=0;i-- {
		if utils.Cancelled(ctx) {return}
		output[counts[arr[i]]-1]=arr[i]
		counts[arr[i]]-=1
	}
	copy(arr,output)

	// fix the array from the start
	for i:=range n {
		if utils.Cancelled(ctx) {return}
		arr[i]+=low
	}
}