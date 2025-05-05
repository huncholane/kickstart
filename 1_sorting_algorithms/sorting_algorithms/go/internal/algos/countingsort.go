package algos

func Countingsort(nums []int) {
    // counting sort
    min, max := nums[0], nums[0]
    for _, num := range nums {
        if num < min {
            min = num
        }
        if num > max {
            max = num
        }
    }

    count := make([]int, max - min + 1)
    for _, num := range nums {
        count[num-min]++
    }

    k := 0
    for i:=range len(count) {
        for count[i] > 0 {
            nums[k] = i + min
            k++
            count[i]--
        }
    }
}