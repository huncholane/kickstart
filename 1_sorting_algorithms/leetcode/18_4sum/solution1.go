package solutions

import "sort"
func fourSum(nums []int, target int) [][]int {
    sort.Ints(nums)
    res:=[][]int{}
    n:=len(nums)

    twoSum:=func(l,src1,src2,target int) [][]int {
        sums:=[][]int{}
        i,j:=l,n-1
        for i<j {
            n1,n2:=nums[i],nums[j]
            val:=n1+n2
            switch {
            case val==target:
                sums=append(sums,[]int{src1,src2,n1,n2})
                i++;j--
                for i<j && nums[i]==n1 {i++}
                for j>i && nums[j]==n2 {j--}
            case val<target:
                i++
            default:
                j--
            }
        }
        return sums
    }
    
    threeSum:=func(l,src,target int) [][]int {
        sums:=[][]int{}
        end:=n-2
        i:=l
        for i<end {
            num:=nums[i]
            sums=append(sums,twoSum(i+1,src,num,target-nums[i])...)
            i+=1
            for i<end && nums[i]==num {i++}
        }
        return sums
    }

    i:=0
    end:=n-3
    for i<end {
        num:=nums[i]
        res=append(res,threeSum(i+1,num,target-nums[i])...)
        i+=1
        for i<end && nums[i]==num {i++}
    }

    return res
}