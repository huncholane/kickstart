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
