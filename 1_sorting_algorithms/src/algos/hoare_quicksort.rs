fn helper(arr: &mut Vec<i32>, start: usize, end: usize) {
    // Leaf job
    if start >= end {
        return;
    }
    // Internal node worker
    let pivotindex = rand::random_range(start..end + 1);
    arr.swap(start, pivotindex);
    let mut smaller = start + 1;
    let mut bigger = end;
    while smaller <= bigger {
        if arr[smaller] < arr[start] {
            smaller += 1;
        } else if arr[bigger] > arr[start] {
            bigger -= 1;
        } else {
            arr.swap(bigger, smaller);
            smaller += 1;
            bigger -= 1;
        }
    }
    arr.swap(start, bigger);
    helper(arr, start, bigger.max(1) - 1);
    helper(arr, smaller + 1, end);
}

pub fn hoare_quicksort(arr: &mut Vec<i32>) {
    let len = arr.len();
    helper(arr, 0, len - 1);
}
