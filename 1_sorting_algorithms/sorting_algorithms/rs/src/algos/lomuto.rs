pub fn lomuto_quicksort(arr: &mut Vec<i32>) {
    let n = arr.len();
    let mut stack = vec![(0, n - 1)];
    while stack.len() > 0 {
        let (l, r) = stack.pop().unwrap();
        let mut i = l;
        for j in l + 1..=r {
            if arr[j] < arr[l] {
                i += 1;
                arr.swap(i, j);
            }
        }
        arr.swap(l, i);
        if l > 0 && l < i - 1 {
            stack.push((l, i - 1));
        }
        if r < n && i + 1 < r {
            stack.push((i + 1, r));
        }
    }
}
