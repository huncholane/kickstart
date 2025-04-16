package utils

import (
	"context"
	"fmt"
	"reflect"
	"runtime"
	"time"
)

type Analyzer struct {
	f func([]int)
	Name string
}

func NewAnalyzer(f func([]int)) *Analyzer {
	name:=runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
	return &Analyzer{f,name}
}

func (a *Analyzer) TimeIt(arr[]int,print bool) time.Duration {
	start:=time.Now()
	a.f(arr)
	t:=time.Since(start)
	if print {
		fmt.Printf("%s took %v, Successful sort: %v\n",a.Name,t,DidSort(arr))
	}
	return t
}

// Times an algorithm on an array given context so it can stop
//	- ctx: Context
//	- arr: The array to sort
func (a *Analyzer) AsyncTimeIt(ctx context.Context,arr[]int) time.Duration {
	start:=time.Now()

	done:=make(chan time.Duration,1)
	go func() {
		a.f(arr)
		close(done)
	}()

	select {
	case<-ctx.Done():
		return -1
	case<-done:
		return time.Since(start)
	}
}

// Describes an algorithm based on the given test config
func (a*Analyzer) Describe(t Test) {
	arr:=CreateArr(t.size,t.left,t.right)
	fmt.Printf("Before sorting: %v\n",arr)
	a.TimeIt(arr,true)
	fmt.Printf("After sorting: %v\n",arr)
	fmt.Printf("Passed %v of %v tests\n",t.Run(),t.numTests)
}

// Uses the default test config to analyze
func (a*Analyzer) DescribeDefault() {
	a.Describe(*DefaultTest(a.f))
}

// Uses a tiny test to describe the algorithm
func (a*Analyzer) DescribeTiny() {
	a.Describe(Test{
		f:a.f,
		numTests: 10,
		size: 10,
		left: -5,
		right: 5,
	})
}

func (a *Analyzer) DefaultTest() {
	DefaultTest(a.f).Run()
}

func TimeCancelable(ctx context.Context, f func(context.Context,[]int),arr []int) time.Duration {
	start:=time.Now()
	f(ctx,arr)
	return time.Since(start)
}

// This does general analysis on a cancelable algorithm
// 	- Runs the algorithm with a small array
// 	- Prints the name, time it took for the small array 
// 	- Then runs tests and prints number passed
func GeneralAnalysisOnCancelable(ctx context.Context,f func(context.Context,[]int)) {
	name:=runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
	fmt.Println("Running general analysis for",name)
	arr:=CreateSymetricArr(10)
	fmt.Println("Before sorting:",arr)
	f(ctx,arr)
	fmt.Println(" After sorting:",arr)
	successfulCount:=TestCancelable(f,100,10,10000,1*time.Millisecond)
	fmt.Println(successfulCount,"of",100,"passed")
}