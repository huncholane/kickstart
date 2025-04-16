package solutions

func twoSum(nums []int, target int) []int {
    table:=make(map[int]int)
    for i,num:=range nums {
        c:=target-num
        if j,ok:=table[c];ok {
            return []int{i,j}
        }
        table[num]=i
    }    
    return []int{}
}