package solutions

import (
    "math/rand"
)

func SortArray(nums []int) []int {
    var helper func(int,int)
    partition:=func(l,r int) int {
        pivot:=nums[rand.Intn(max(r-l,1))+l]
        i,j:=l-1,r+1
        for {
            i++
            for nums[i]<pivot {
                i++
            }
            j--
            for nums[j]>pivot {
                j--
            }
            if i>=j {break}
            nums[i],nums[j]=nums[j],nums[i]
        }
        return j
    }
    helper=func(l,r int) {
        if l>=r {return}
        pi:=partition(l,r)
        helper(l,pi)
        helper(pi+1,r)
    }
    helper(0,len(nums)-1)
    return nums
}