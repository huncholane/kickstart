package solutions

import (
	"fmt"
	"sort"
)

func threeSumMulti(arr []int, target int) int {
    mod:=1_000_000_007
    sort.Ints(arr)
    n:=len(arr)
    res:=0%mod
    fmt.Println(n)
    for m:=2;m<n;m++ {
        i,j:=0,m-1
        for i<j {
            ival,jval:=arr[i],arr[j]
            s:=arr[i]+arr[j]+arr[m]
            if s>target {
                j--
            } else if s<target {
                i++
            } else {
                icount,jcount:=0,0
                if arr[i]==arr[j] {
                    // n choose 2 where n is j-i+1
                    nc2:=(j-i+1)*(j-i)/2
                    res+=nc2%mod
                    res%=mod
                    break
                } else {
                    for i<m && arr[i]==ival {i++;icount++}
                    for j>0 && arr[j]==jval {j--;jcount++}
                    addval:=icount*jcount
                    res+=addval%mod
                    res%=mod
                }
            }
        }
    } 
    return res
}