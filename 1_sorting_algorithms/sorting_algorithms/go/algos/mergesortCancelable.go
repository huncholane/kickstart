package algos

import (
	"context"
	"sortingalgos/utils"
)

// Mergesort helper that enables timeout
func helperCancelable(ctx context.Context,arr []int,l int, r int) {
	if l>=r {
		return
	}
	mid:=l+(r-l)/2
	if utils.Cancelled(ctx) {return}
	helperCancelable(ctx,arr,l,mid)
	if utils.Cancelled(ctx) {return}
	helperCancelable(ctx,arr,mid+1,r)
	var i,j=l,mid+1
	aux:=make([]int,0,r-l+1)
	for i<=mid && j<=r {
		if utils.Cancelled(ctx) {return}
		if arr[i]<=arr[j] {
			aux=append(aux,arr[i])
			i++
		} else {
			aux=append(aux,arr[j])
			j++
		}
	}
	for i<=mid {
		if utils.Cancelled(ctx) {return}
		aux=append(aux,arr[i])
		i++
	}
	for j<=r {
		if utils.Cancelled(ctx) {return}
		aux=append(aux,arr[j])
		j++
	}
	if utils.Cancelled(ctx) {return}
	copy(arr[l:r+1],aux)
}

// Mergesort that can be canceled
func MergesortCancelable(ctx context.Context,arr []int) {
	if len(arr)==0 {
		return
	}
	helperCancelable(ctx,arr,0,len(arr)-1)
}