fn heapify_down(arr: &mut Vec<i32>, start: usize, end: usize) {
    let c1 = (start + 1) * 2 - 1;
    let c2 = c1 + 1;
    if c1 > end {
        return;
    }
    let child = match c1 == end || arr[c1] > arr[c2] {
        true => c1,
        false => c2,
    };
    if arr[child] > arr[start] {
        arr.swap(child, start);
        heapify_down(arr, child, end);
    }
}

fn build_heap(arr: &mut Vec<i32>) {
    for i in (0..arr.len() / 2).rev() {
        heapify_down(arr, i, arr.len() - 1);
    }
}

fn extract(arr: &mut Vec<i32>, i: usize) {
    arr.swap(0, i);
    heapify_down(arr, 0, i - 1);
}

pub fn heapsort(arr: &mut Vec<i32>) {
    build_heap(arr);
    for i in (1..arr.len()).rev() {
        extract(arr, i);
    }
}
