package main

import (
	"context"
	"sortingalgos/internal/algos"
	"sortingalgos/internal/cancelable"
	"sortingalgos/internal/utils"
)

func main() {
	utils.GeneralAnalysis(algos.Quicksort3)
	utils.GeneralAnalysisOnCancelable(context.Background(),cancelable.Quicksort3)
}