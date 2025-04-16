package algos

import (
	"math/rand"
)

type pair struct {
	l int
	r int
}

// lomutoPartition paritions an array using Lomuto's method
func lomutoPartition(arr[]int,l,r int) int {
	pi:=rand.Intn(r-l)+l
	arr[l],arr[pi]=arr[pi],arr[l]
	i:=l
	for j:=l+1;j<=r;j++ {
		if arr[j]<arr[l] {
			i++
			arr[i],arr[j]=arr[j],arr[i]
		}
	}
	arr[l],arr[i]=arr[i],arr[l]
	return i
}

func Lomutosort(arr[]int) {
	n:=len(arr)
	stack:=make([]pair,0,n)
	stack=append(stack,pair{l:0,r:n-1})
	for len(stack)>0 {
		n=len(stack)
		p:=stack[n-1]
		stack=stack[:n-1]
		if p.l>=p.r {continue}
		i:=lomutoPartition(arr,p.l,p.r)
		stack=append(stack,pair{l:p.l,r:i-1})
		stack=append(stack,pair{l:i+1,r:p.r})
	}
}

func hoarePartition(arr[]int,l,r int) int {
	var pivot int
	if r-l==1 {
		pivot=arr[l]
	} else {
		pivot=arr[rand.Intn(r-l-1)+l]
	}
	i,j:=l-1,r+1
	for {
		i++
		for arr[i]<pivot {
			i++
		}
		j--
		for arr[j]>pivot {
			j--
		}
		if i>=j {
			break
		}
		arr[i],arr[j]=arr[j],arr[i]
	}
	return j
}

func Hoaresort(arr[]int) {
	n:=len(arr)
	stack:=make([]pair,0,n)
	stack=append(stack,pair{l:0,r:n-1})
	for len(stack)>0 {
		n=len(stack)
		p:=stack[n-1]
		stack=stack[:n-1]
		if p.l>=p.r {continue}
		i:=hoarePartition(arr,p.l,p.r)
		stack=append(stack,pair{l:p.l,r:i})
		stack=append(stack,pair{l:i+1,r:p.r})
	}
}

func partition3(arr[]int,l,r int) (int,int){
	// pivot:=arr[rand.Intn(r-l)+l]
	pivot:=arr[l+(r-l)/2]
	i,j,k:=l,l,r
	for j<=k {
		if arr[j]<pivot {
			arr[i],arr[j]=arr[j],arr[i]
			i++
			j++
		} else if arr[j]==pivot {
			j++
		} else {
			arr[j],arr[k]=arr[k],arr[j]
			k--
		}
	}
	return i,k
}

func Quicksort3(arr[]int) {
	n:=len(arr)
	stack:=make([]pair,0,n)
	stack=append(stack,pair{l:0,r:n-1})
	for len(stack)>0 {
		n=len(stack)
		p:=stack[n-1]
		stack=stack[:n-1]
		if p.l>=p.r {continue}
		l,r:=partition3(arr,p.l,p.r)
		stack=append(stack,pair{l:p.l,r:l-1})
		stack=append(stack,pair{l:r+1,r:p.r})
	}
}