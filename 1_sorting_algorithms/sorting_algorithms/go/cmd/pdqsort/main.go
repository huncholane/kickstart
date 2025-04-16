package main

import (
	"sortingalgos/internal/algos"
	"sortingalgos/internal/utils"
)

func main() {
	utils.NewAnalyzer(algos.Pdqsort).DescribeTiny()
}