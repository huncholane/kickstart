package solutions

import (
    "sort"
)

func threeSumSmaller(nums []int, target int) int {
    sort.Ints(nums)
    n:=len(nums)
    res:=0
    for m:=range n {
        i,j:=0,m-1
        for i<j {
            s:=nums[i]+nums[j]+nums[m]
            if s>=target {
                j--
            } else {
                res+=j-i
                i++
            }
        }
    }
    return res
}