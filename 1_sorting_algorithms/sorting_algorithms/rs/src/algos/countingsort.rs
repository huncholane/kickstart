pub fn countingsort(arr: &mut Vec<i32>) {
    // init aux
    let (mut l, mut r) = (arr[0], arr[0]);
    for i in 1..arr.len() {
        if arr[i] < l {
            l = arr[i];
        } else if arr[i] > r {
            r = arr[i];
        }
    }
    let k = r - l;
    let mut aux = vec![0; k as usize + 1];
    for num in &*arr {
        aux[(*num - l) as usize] += 1;
    }
    // dump into arr
    let mut i = 0;
    for num in 0..k + 1 {
        while aux[num as usize] > 0 {
            arr[i] = num + l;
            i += 1;
            aux[num as usize] -= 1;
        }
    }
}
