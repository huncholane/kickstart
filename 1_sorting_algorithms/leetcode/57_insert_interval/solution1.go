package solution

import "sort"

func insert(intervals [][]int, newInterval []int) [][]int {
	// just append and merge
	intervals = append(intervals, newInterval)
	n := len(intervals)
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	res := [][]int{intervals[0]}
	for i := 1; i < n; i++ {
		last := res[len(res)-1]
		cur := intervals[i]
		if last[1] >= cur[0] {
			// overlap
			res[len(res)-1][1] = max(cur[1], last[1])
		} else {
			res = append(res, cur)
		}
	}
	return res
}
