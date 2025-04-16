package solutions

import "sort"

func intersection(nums1 []int, nums2 []int) []int {
    n1,n2:=len(nums1),len(nums2)
    res:=make([]int,0,min(len(nums1),len(nums2)))

    // presort
    sort.Ints(nums1)
    sort.Ints(nums2)
    
    i,j:=0,0
    for i<n1 && j<n2 {
        if nums1[i]<nums2[j] {
            i++
        } else if nums1[i]>nums2[j] {
            j++
        } else {
            res=append(res,nums1[i])
            i++
            for i<n1 && nums1[i]==nums1[i-1] {i++}
            j++
            for j<n2 && nums2[j]==nums2[j-1] {j++}
        }
    }
    return res
}