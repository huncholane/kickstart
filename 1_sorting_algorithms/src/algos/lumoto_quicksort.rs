fn helper(arr: &mut Vec<i32>, start: usize, end: usize) {
    // Leaf job
    if start >= end {
        return;
    }
    // Internal node worker
    let pivotindex = rand::random_range(start..end + 1);
    arr.swap(start, pivotindex);
    let mut smaller = start;
    for bigger in start + 1..end + 1 {
        if arr[bigger] < arr[start] {
            smaller += 1;
            arr.swap(bigger, smaller);
        }
    }
    arr.swap(start, smaller);
    helper(
        arr,
        start,
        match smaller == 0 {
            true => smaller,
            false => smaller - 1,
        },
    );
    helper(arr, smaller + 1, end);
}

pub fn lumoto_quicksort(arr: &mut Vec<i32>) {
    let len = arr.len();
    helper(arr, 0, len - 1);
}
