package solutions

import (
    "sort"
    "math"
)
func threeSumClosest(nums []int, target int) int {
    sort.Ints(nums)
    closestdist:=math.MaxInt
    var answer int
    n:=len(nums)

    // threesum template 
    for m:=range n {
        i,j:=0,m-1
        for i<j {
            s:=nums[i]+nums[j]+nums[m]
            if s==target {
                return target
            } else if s>target {
                if s-target<closestdist {
                    closestdist=s-target
                    answer=s
                }
                j--
            } else {
                if target-s<closestdist {
                    closestdist=target-s
                    answer=s
                }
                i++
            }
        }
    }
    return answer
}