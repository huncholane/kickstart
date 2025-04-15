package utils

import (
	"math/rand"
)

func DidSort(arr[]int) bool {
	for i:=range len(arr)-1 {
		if arr[i]>arr[i+1] {
			return false
		}
	}
	return true
}

// Creates an array of size with random values [left,right]
func CreateArr(size int,left int,right int) []int {
	arr:=make([]int,size)
	for i:=range size {
		arr[i]=rand.Intn(1+right-left)+left
	}
	return arr
}

// Creates a symetric array of random values just given size
func CreateSymetricArr(size int) []int{
	l:=size/2-size
	r:=size/2
	return CreateArr(size,l,r)
}

