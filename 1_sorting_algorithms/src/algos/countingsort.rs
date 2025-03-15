pub fn countingsort(arr: &mut Vec<i32>) {
    // init aux
    let k = arr.iter().max().unwrap();
    let mut aux = vec![0; *k as usize + 1];
    for num in &*arr {
        aux[*num as usize] += 1;
    }
    // dump into arr
    let mut i = 0;
    for num in 0..k + 1 {
        while aux[num as usize] > 0 {
            arr[i] = num;
            i += 1;
            aux[num as usize] -= 1;
        }
    }
}
