package main

import (
	"context"
	"fmt"
	"reflect"
	"runtime"
	"sort"
	"sortingalgos/internal/cancelable"
	"sortingalgos/internal/utils"
	"time"
)

type Result struct {
	Name string
	Dur time.Duration
}

func main() {
	var results []Result
	n:=1000000
	l:=-n/2
	r:=n/2
	timeout:=500*time.Millisecond
	fmt.Printf("Comparing Algos with n=%d [%d, %d] and a timeout of %v\n",n,l,r,timeout)
	arr:=utils.CreateArr(n,l,r)
	fmt.Println("Created test array")
	funcs:=[]func(context.Context,[]int){
		cancelable.Mergesort,
		cancelable.CountingSort,
		cancelable.Pdqsort,
		cancelable.Quicksort3,
		cancelable.Hoaresort,
		cancelable.Lomutosort,
		cancelable.Heapsort,
	}

	for _, f := range funcs {
		// Make a copy of the array so each analyzer uses the same data
		tmp:=make([]int, len(arr))
		copy(tmp,arr)

		name:=runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
		fmt.Println("Copied test array for",name)

		ctx,cancel:=context.WithTimeout(context.Background(),timeout)
		defer cancel()
		
		start:=time.Now()
		f(ctx,arr)		
		dur:=time.Since(start)
		if ctx.Err() !=nil {
			fmt.Println("❌",name,"timed out")
		} else {
			results=append(results,Result{Dur:dur,Name:name})
		}
	}

	fmt.Println()

	// Sort the results
	sort.Slice(results,func(i,j int) bool {
		return results[i].Dur<results[j].Dur
	})

	// Print the results
	for i,res:=range results {
		switch i {
		case 0:
			fmt.Printf("🥇 %v %v\n",res.Dur,res.Name)
		case 1:
			fmt.Printf("🥈 %v %v\n",res.Dur,res.Name)
		case 2:
			fmt.Printf("🥉 %v %v\n",res.Dur,res.Name)
		default:
			fmt.Printf("%d %v %v\n",i,res.Dur,res.Name)
		}
	}
}