package utils

import (
	"context"
	"time"
)

type Test struct {
	f func([]int)
	numTests int
	size int
	left int
	right int
}

// DefaultTest initializes a Test with:
//   - 10 tests
//   - Range: -100 to 100
//   - Size: 100
func DefaultTest(f func([]int)) *Test {
	return &Test{f:f,numTests:10,size:100,left:-100,right:100}
}

// Run tests using the test config
func (t *Test) Run() int {
	passed:=0
	for range t.numTests {
		arr:=CreateArr(t.size,t.left,t.right)
		t.f(arr)
		if DidSort(arr) {
			passed+=1
		}
	}
	return passed
}

// Test a cancelable version runs the number of tests-1 and 
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