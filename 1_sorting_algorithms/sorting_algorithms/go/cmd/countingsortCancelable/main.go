package main

import (
	"context"
	"sortingalgos/internal/cancelable"
	"sortingalgos/internal/utils"
)

func main() {
	utils.GeneralAnalysisOnCancelable(context.Background(),cancelable.CountingSort)
}