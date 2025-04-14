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