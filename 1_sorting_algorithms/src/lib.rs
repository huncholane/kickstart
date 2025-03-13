pub fn selection_sort(arr: &mut Vec<i32>) {
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

pub fn bubble_sort(arr: &mut Vec<i32>) {
    for i in (0..arr.len()).rev() {
        for j in 1..i {
            if arr[j] < arr[j - 1] {
                arr.swap(j, j - 1);
            }
        }
    }
}

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
