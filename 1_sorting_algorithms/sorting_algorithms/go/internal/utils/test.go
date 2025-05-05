package utils

import (
	"context"
	"time"
)

// Test tests an algorithm
//	- f: The algorithm to test
//	- arrSize: Size of the arrays
//	- testCount: How many tests to perform
func Test(f func([]int),arrSize,testCount int) int {
	successCount:=0
	for range testCount {
		arr:=CreateSymetricArr(arrSize)
		f(arr)
		if DidSort(arr) {
			successCount+=1
		}
	}
	return successCount
}

// TestCancelable tests a cancelable version runs the number of tests-1 and 
// checks if the function is cancelable
//	- f [func(context.Context,[]int)]: The cancelable algorithm to test
//	- arrSize [int]: Size of the arrays
//	- testCount [int]: How many tests to perform
//	- timeoutArrSize [int]: The length of the array that should cause a timeout
//	- timeout [time.Duration]: The timeout
func TestCancelable(f func(context.Context,[]int),arrSize,testCount,timeoutArrSize int,timeout time.Duration) int {
	successCount:=0
	for range testCount-1 {
		arr:=CreateSymetricArr(arrSize)
		f(context.Background(),arr)
		if DidSort(arr) {
			successCount+=1
		}
	}

	// Test the timeout functionality
	ctx,cancel:=context.WithTimeout(context.Background(),timeout)
	defer cancel()
	f(ctx,CreateSymetricArr(timeoutArrSize))
	if Cancelled(ctx) {
		successCount++
	}

	return successCount
}