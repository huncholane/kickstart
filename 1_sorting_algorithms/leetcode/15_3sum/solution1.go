package solutions

import "sort"
func threeSum(nums []int) [][]int {
    n:=len(nums)
    sort.Ints(nums)
    res:=[][]int{}
    
    twoSum:=func(l,r,src int) [][]int {
        target:=-src
        sums:=[][]int{}
        i,j:=l,r
        for i<j {
            n1,n2:=nums[i],nums[j]
            val:=n1+n2
            switch {
            case val==target:
                sums=append(sums,[]int{src,n1,n2})
                i++
                for i<n && nums[i]==n1 {i++}
                j--
                for j>=0 && nums[j]==n2 {j--}
            case val<target:
                i++
            default:
                j--
            } 
        }
        return sums
    }

    i:=0
    for i<n-2 {
        src:=nums[i]
        res=append(res,twoSum(i+1,n-1,src)...)
        i++
        for i<n-2 && nums[i]==src {
            i++
        }
    }

    return res
}