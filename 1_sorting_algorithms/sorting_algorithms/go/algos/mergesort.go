package algos

func helper(arr []int,l int, r int) {
	if l>=r {
		return
	}
	mid:=l+(r-l)/2
	helper(arr,l,mid)
	helper(arr,mid+1,r)
	var i,j=l,mid+1
	aux:=make([]int,0,r-l+1)
	for i<=mid && j<=r {
		if arr[i]<=arr[j] {
			aux=append(aux,arr[i])
			i++
		} else {
			aux=append(aux,arr[j])
			j++
		}
	}
	for i<=mid {
		aux=append(aux,arr[i])
		i++
	}
	for j<=r {
		aux=append(aux,arr[j])
		j++
	}
	copy(arr[l:r+1],aux)
}

func Mergesort(arr []int) {
	if len(arr)==0 {
		return
	}
	helper(arr,0,len(arr)-1)
}