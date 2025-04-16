package solutions

import (
	"sort"
)

func twoSumLessThanK(nums []int, k int) int {
    n:=len(nums)-1
    sort.Ints(nums)
    
    i,j:=0,n-1
    maxval:=-1
    for i<j {
        n1,n2:=nums[i],nums[j]
        val:=n1+n2
        if val>=k {
            j-- // eliminate rightmost col
        } else {
            maxval=max(maxval,val)
            i++ // eliminate top row
        }
    }
    return maxval
}