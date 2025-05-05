package solutions

func sortColors(nums []int)  {
    i,j,k:=0,0,len(nums)-1
    for j<=k {
        switch {
            case nums[j]<1:
            nums[i],nums[j]=nums[j],nums[i]
            i++;j++
            case nums[j]==1:
            j++
            default:
            nums[j],nums[k]=nums[k],nums[j]
            k--
        }
    }
}