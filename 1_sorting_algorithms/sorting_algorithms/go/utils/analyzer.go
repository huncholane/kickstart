package utils

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

type Analyzer struct {
	f func([]int)
}

func NewAnalyzer(f func([]int)) *Analyzer {
	return &Analyzer{f}
}

func (a *Analyzer) TimeIt(arr[]int) {
	name:=runtime.FuncForPC(reflect.ValueOf(a.f).Pointer()).Name()
	start:=time.Now()
	a.f(arr)
	fmt.Printf("%s took %v, Successful sort: %v\n",name,time.Since(start),DidSort(arr))
}

// Describes an algorithm based on the given test config
func (a*Analyzer) Describe(t Test) {
	arr:=CreateArr(t.size,t.left,t.right)
	fmt.Printf("Before sorting: %v\n",arr)
	a.TimeIt(arr)
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