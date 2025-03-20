pub fn hoare_quicksort(arr: &mut Vec<i32>) {
    let mut stack = vec![(0, arr.len() - 1)];
    while stack.len() > 0 {
        let (l, r) = stack.pop().unwrap();
        if l >= r {
            continue;
        }
        let pivot = arr[(l + r) / 2];
        let (mut i, mut j) = (l - 1, r + 1);
        loop {
            i += 1;
            while arr[i] < pivot {
                i += 1;
            }
            j -= 1;
            while arr[j] > pivot {
                j -= 1;
            }
            if i >= j {
                break;
            }
            arr.swap(i, j);
        }
        stack.push((l, j));
        stack.push((j + 1, r));
    }
}
