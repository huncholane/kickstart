package main

import (
	"fmt"
	"sortingalgos/algos"
	"sortingalgos/utils"
	"time"
)

func main() {
	done:=make(chan struct{})
	arr:=utils.CreateSymetricArr(1000000000)
	a:=utils.NewAnalyzer(algos.CountingSort)
	go func() {
		a.TimeIt(arr,true)	
		close(done)
	}()
	fmt.Println("sadfsf")
	select {
	case <-done:
		fmt.Println("Done")
	case <-time.After(10*time.Millisecond):
		fmt.Println("Took too long")
	}
}