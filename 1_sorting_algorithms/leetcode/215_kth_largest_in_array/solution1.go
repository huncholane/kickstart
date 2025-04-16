package solutions

import "math/rand"

func findKthLargest(nums []int, k int) int {
    var qs func(int,int) int
    target:=len(nums)-k
    partition:=func(l,r int) (int,int) {
        pivot:=nums[rand.Intn(r-l+1)+l]
        i,j,k:=l,l,r
        for j<=k {
            switch {
                case nums[j]<pivot:
                nums[i],nums[j]=nums[j],nums[i]
                i++;j++
                case nums[j]==pivot:
                j++
                default:
                nums[j],nums[k]=nums[k],nums[j]
                k--
            }
        }
        return i,k
    }
    qs=func(l,r int) int {
        pl,pr:=partition(l,r)
        switch {
            case target<pl:
            return qs(l,pl-1)
            case target>pr:
            return qs(pr+1,r)
            default:
            return nums[target]
        }
    }
    return qs(0,len(nums)-1)
}