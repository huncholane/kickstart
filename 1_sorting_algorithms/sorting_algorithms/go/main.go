package main

import (
	"context"
	"fmt"
	"reflect"
	"runtime"
	"sort"
	"sortingalgos/algos"
	"sortingalgos/utils"
	"time"
)

type Result struct {
	Name string
	Dur time.Duration
}

func main() {
	var results []Result
	n:=1000000000
	l:=n/2-n
	r:=n/2
	fmt.Printf("Comparing Algos with n=%d [%d, %d]\n",n,l,r)
	arr:=utils.CreateArr(n,l,r)
	timeout:=10*time.Millisecond
	funcs:=[]func(context.Context,[]int){
		algos.MergesortCancelable,
	}

	for _, f := range funcs {
		// Make a copy of the array so each analyzer uses the same data
		tmp:=make([]int, len(arr))
		copy(tmp,arr)

		name:=runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()

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