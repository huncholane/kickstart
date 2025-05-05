pub fn selectionsort(arr: &mut Vec<i32>) {
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
