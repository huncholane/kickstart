fn partition(arr: &mut Vec<i32>, l: usize, r: usize) -> usize {
    let mid = (l + r) / 2;
    let pi = rand::random_range(l..r + 1);
    arr.swap(pi, mid);
    let (mut i, mut j) = (l - 1, r + 1);
    loop {
        i += 1;
        while arr[i] < arr[mid] {
            i += 1;
        }
        j -= 1;
        while arr[j] > arr[mid] {
            j -= 1;
        }
        if i >= j {
            return j;
        }
        arr.swap(i, j);
    }
}
fn helper(arr: &mut Vec<i32>, l: usize, r: usize) {
    // Leaf job
    if l >= r {
        return;
    }
    // Internal node worker
    let pi = partition(arr, l, r);
    helper(arr, l, pi.max(1) - 1);
    helper(arr, pi + 1, r);
}

pub fn hoare_quicksort(arr: &mut Vec<i32>) {
    let len = arr.len();
    helper(arr, 0, len - 1);
}
