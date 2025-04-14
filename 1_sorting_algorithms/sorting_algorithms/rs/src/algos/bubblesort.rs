pub fn bubble_sort(arr: &mut Vec<i32>) {
    for i in (0..arr.len()).rev() {
        for j in 1..i {
            if arr[j] < arr[j - 1] {
                arr.swap(j, j - 1);
            }
        }
    }
}
