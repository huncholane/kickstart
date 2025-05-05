package solutions

import "sort"

func mergeLineSweep(intervals [][]int) [][]int {
	n := len(intervals)
	res := make([][]int, 0, n)

	// presort
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	// line sweep
	res = append(res, intervals[0])
	for i := 1; i < n; i++ {
		if res[len(res)-1][1] < intervals[i][0] {
			res = append(res, intervals[i])
		} else {
			res[len(res)-1][1] = max(res[len(res)-1][1], intervals[i][1])
		}
	}
	return res
}
