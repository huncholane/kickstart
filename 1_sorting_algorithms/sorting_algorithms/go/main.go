package main

import (
	"context"
	"fmt"
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
	n:=100000000
	l:=n/2-n
	r:=n/2
	fmt.Printf("Comparing Algos with n=%d [%d, %d]\n",n,l,r)
	arr:=utils.CreateArr(n,l,r)
	timeout:=1000*time.Millisecond
	funcs:=[]func([]int){
		algos.Mergesort,
		algos.CountingSort,
		sort.Ints,
	}
	for _, f := range funcs {
		tmp:=make([]int, len(arr))
		copy(tmp,arr)
		a:=utils.NewAnalyzer(f)

		ctx,cancel:=context.WithTimeout(context.Background(),timeout)
		defer cancel()
		d:=a.AsyncTimeIt(ctx,tmp)
		if d<0{
			fmt.Printf("%s timed out\n",a.Name)
			d=timeout
		}
		results=append(results,Result{Name:a.Name,Dur:d})
	}
	sort.Slice(results,func(i,j int) bool {
		return results[i].Dur<results[j].Dur
	})
	for i,res:=range results {
		if res.Dur==timeout {
			fmt.Printf("❌ %v timed out\n",res.Name)
			continue
		}
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