package utils

import (
	"context"
	"fmt"
	"reflect"
	"runtime"
	"time"
)


func TimeCancelable(ctx context.Context, f func(context.Context,[]int),arr []int) time.Duration {
	start:=time.Now()
	f(ctx,arr)
	return time.Since(start)
}

// GeneralAnalysis  does general analysis on an algorithm
// 	1. Runs the algorithm with a small array
// 	2. Prints the name, time it took for the small array 
// 	3. Then runs tests and prints number passed
func GeneralAnalysis(f func([]int)) {
	name:=runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
	fmt.Println("Running general analysis for",name)
	arr:=CreateSymetricArr(10)
	fmt.Println("Before sorting:",arr)
	f(arr)
	fmt.Println(" After sorting:",arr)
	successfulCount:=Test(f,100,10)
	fmt.Println(successfulCount,"of",10,"passed")
}

// GeneralAnalysisOnCancelable does general analysis on a cancelable algorithm
// 	1. Runs the algorithm with a small array
// 	2. Prints the name, time it took for the small array 
// 	3. Then runs tests and prints number passed
func GeneralAnalysisOnCancelable(ctx context.Context,f func(context.Context,[]int)) {
	name:=runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
	fmt.Println("Running general analysis for",name)
	arr:=CreateSymetricArr(10)
	fmt.Println("Before sorting:",arr)
	f(ctx,arr)
	fmt.Println(" After sorting:",arr)
	successfulCount:=TestCancelable(f,100,10,10000,1*time.Millisecond)
	fmt.Println(successfulCount,"of",10,"passed")
}