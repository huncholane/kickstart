package main

import (
	"fmt"
	"math/rand"
)

func countingsort(arr []int) {
	low:=arr[0]
	high:=arr[0]
	n:=len(arr)
	for i:=range n {
		if arr[i]<low {
			low = arr[i]
		} else if arr[i]>high {
			high=arr[i]
		}
	}

	// make array start from 0
	for i:=range n {
		arr[i]-=low
	}
	k:=high-low

	// init aux count array
	aux:=make([]int,k+1)
	for i:=range n {
		aux[arr[i]]+=1
	}

	// cummulate the sums to index correctly
	for i:=1;i<k+1;i++ {
		aux[i]+=aux[i-1]
	}

	// store output in reverse order and store into original array
	output:=make([]int,n)
	for i:=n-1;i>=0;i-- {
		output[aux[arr[i]]-1]=arr[i]
		aux[arr[i]]-=1
		i-=1
	}
	copy(arr,output)

	// fix the array from the start
	for i:=range n {
		arr[i]+=low
	}
}

func main() {
	n:=10
	arr:=make([]int,n)
	for i:=range n {
		arr[i]=rand.Intn(n)
	}
	fmt.Println(arr)
	countingsort(arr)
	fmt.Println(arr)
}