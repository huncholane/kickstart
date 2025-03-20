pub fn lomuto_quicksort(arr: &mut Vec<i32>) {
    let mut stack = vec![(0, arr.len() - 1)];
    while stack.len() > 0 {
        let (l, r) = stack.pop().unwrap();
        if l >= r {
            continue;
        }
        let mut i = l;
        for j in l + 1..=r {
            if arr[j] < arr[l] {
                i += 1;
                arr.swap(i, j);
            }
        }
        arr.swap(l, i);
        if l > 1 {
            stack.push((l, i - 1));
        }
        stack.push((i + 1, r));
    }
}
