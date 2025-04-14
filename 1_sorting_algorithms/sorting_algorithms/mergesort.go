package main

import (
	"fmt"
	"math/rand"
)

func helper(arr []int,l int, r int) {
	if l==r {
		return
	}
	mid:=l+(r-l)/2
	helper(arr,l,mid)
	helper(arr,mid+1,r)
	var i,j=l,mid+1
	var aux []int
	for i<=mid && j<=r {
		if arr[i]<=arr[j] {
			aux=append(aux,arr[i])
			i++
		} else {
			aux=append(aux,arr[j])
			j++
		}
	}
	for i<=mid {
		aux=append(aux,arr[i])
		i++
	}
	for j<=r {
		aux=append(aux,arr[j])
		j++
	}
	copy(arr[l:r+1],aux)
}

func mergesort(arr []int) {
	helper(arr,0,len(arr)-1)
}

func main() {
	n:=10
	arr:=make([]int,n)
	for i:=0;i<n;i++ {
		arr[i]=rand.Intn(n)
	}
	fmt.Println(arr)
	mergesort(arr)
	fmt.Println(arr)
}