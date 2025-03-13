pub fn selection_sort(arr: &mut Vec<i32>) {
    for i in 0..arr.len() {
        let mut minind = i;
        for j in i + 1..arr.len() {
            if arr[j] < arr[minind] {
                minind = j;
            }
        }
        arr.swap(i, minind);
    }
}

pub fn bubble_sort(arr: &mut Vec<i32>) {
    for i in (0..arr.len()).rev() {
        for j in 1..i {
            if arr[j] < arr[j - 1] {
                arr.swap(j, j - 1);
            }
        }
    }
}

pub fn insertion_sort(arr: &mut Vec<i32>) {
    for i in 0..arr.len() {
        let mut j = i;
        let tmp = arr[i];
        while j > 0 && arr[j - 1] > tmp {
            arr[j] = arr[j - 1];
            j -= 1;
        }
        arr[j] = tmp;
    }
}

pub fn mergesort(arr: &mut Vec<i32>, start: usize, end: usize) {
    // Leaf worker job
    if start == end {
        return;
    }
    // Internal node manager job
    let mid = (start + end) / 2;
    mergesort(arr, start, mid);
    mergesort(arr, mid + 1, end);
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
