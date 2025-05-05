package solutions

func arraysIntersection(arr1 []int, arr2 []int, arr3 []int) []int {
	intersect2 := func(a1, a2 []int) []int {
		n1, n2 := len(a1), len(a2)
		res := make([]int, 0, min(n1, n2))
		i, j := 0, 0
		for i < n1 && j < n2 {
			if a1[i] < a2[j] {
				i++
			} else if a1[i] > a2[j] {
				j++
			} else {
				res = append(res, a1[i])
				i++
				j++
			}
		}
		return res
	}
	a := intersect2(arr1, arr2)
	return intersect2(a, arr3)
}
