pub fn helper(arr: &mut Vec<i32>, start: usize, end: usize) {
    // Leaf worker job
    if start == end {
        return;
    }
    // Internal node manager job
    let mid = (start + end) / 2;
    helper(arr, start, mid);
    helper(arr, mid + 1, end);
    let (mut i, mut j) = (start, mid + 1);
    let len = end - start + 1;
    let mut aux: Vec<i32> = Vec::with_capacity(len);
    while i <= mid && j <= end {
        if arr[i] >= arr[j] {
            aux.push(arr[j]);
            j += 1;
        } else {
            aux.push(arr[i]);
            i += 1;
        }
    }
    // Gather leftovers
    while i <= mid {
        aux.push(arr[i]);
        i += 1;
    }
    while j <= end {
        aux.push(arr[j]);
        j += 1;
    }
    // Copy into original array
    for (i, num) in aux.iter().enumerate() {
        arr[start + i] = *num;
    }
}

pub fn mergesort(arr: &mut Vec<i32>) {
    let len = arr.len();
    helper(arr, 0, len - 1);
}
