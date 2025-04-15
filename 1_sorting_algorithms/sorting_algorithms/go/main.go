package main

import (
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
	timeout:=10*time.Millisecond
	funcs:=[]func([]int){
		algos.Mergesort,
		algos.CountingSort,
		sort.Ints,
	}

	for _, f := range funcs {
		// Make a copy of the array so each analyzer uses the same data
		tmp:=make([]int, len(arr))
		copy(tmp,arr)

		// Initialize the analyzer
		a:=utils.NewAnalyzer(f)

		// Make a channel to store the result
		done:=make(chan Result)
		go func() {
			d:=a.TimeIt(tmp,false)
			done<-Result{Dur:d,Name:a.Name}
		}()

		// Save results
		select {
		case <-time.After(timeout):
			results=append(results,Result{Dur:timeout,Name:a.Name})
		case res:=<-done:
			results = append(results, res)
		}
	}

	// Sort the results
	sort.Slice(results,func(i,j int) bool {
		return results[i].Dur<results[j].Dur
	})

	// Print the results
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