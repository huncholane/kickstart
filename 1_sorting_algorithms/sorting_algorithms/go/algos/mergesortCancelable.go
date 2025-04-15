package algos

import "context"

// Mergesort helper that enables timeout
func helperCancelable(ctx context.Context,arr []int,l int, r int) {
	if l>=r {
		return
	}
	mid:=l+(r-l)/2
	select {
	case <-ctx.Done():
		return
	default:
	}
	helperCancelable(ctx,arr,l,mid)
	select {
	case <-ctx.Done():
		return
	default:
	}
	helperCancelable(ctx,arr,mid+1,r)
	var i,j=l,mid+1
	aux:=make([]int,0,r-l+1)
	for i<=mid && j<=r {
		select {
		case <-ctx.Done():
			return
		default:
		}
		if arr[i]<=arr[j] {
			aux=append(aux,arr[i])
			i++
		} else {
			aux=append(aux,arr[j])
			j++
		}
	}
	for i<=mid {
		select {
		case <-ctx.Done():
			return
		default:
		}
		aux=append(aux,arr[i])
		i++
	}
	for j<=r {
		select {
		case <-ctx.Done():
			return
		default:
		}
		aux=append(aux,arr[j])
		j++
	}
	select {
	case <-ctx.Done():
		return
	default:
	}
	copy(arr[l:r+1],aux)
}

// Mergesort that can be canceled
func MergesortCancelable(ctx context.Context,arr []int) {
	if len(arr)==0 {
		return
	}
	helperCancelable(ctx,arr,0,len(arr)-1)
}