package main

import (
	"context"
	"sortingalgos/internal/algos"
	"sortingalgos/internal/cancelable"
	"sortingalgos/internal/utils"
)

func main() {
	utils.GeneralAnalysis(algos.CountingSort)
	utils.GeneralAnalysisOnCancelable(context.Background(),cancelable.CountingSort)
}