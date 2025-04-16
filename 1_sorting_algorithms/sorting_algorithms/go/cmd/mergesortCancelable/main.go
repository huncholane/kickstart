package main

import (
	"context"
	"fmt"
	"sortingalgos/src/algos"
	"sortingalgos/src/utils"
	"time"
)

func main() {
	size:=10
	timeout:=10*time.Millisecond
	ctx,cancel:=context.WithTimeout(context.Background(),timeout)
	defer cancel()
	arr:=utils.CreateSymetricArr(size)
	algos.MergesortCancelable(ctx,arr)
	switch ctx.Err() {
	case nil:
		fmt.Println("Successfully sorted the Array")
		fmt.Println(arr)
	default:
		fmt.Println("Timed out")
	}
}