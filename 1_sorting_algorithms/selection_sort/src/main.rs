use std::time::Instant;

fn selection_sort(arr: &mut Vec<i32>) {
    for i in 0..arr.len() {
        let mut minval = arr[i];
        let mut minind = i;
        for j in i + 1..arr.len() {
            if arr[j] < minval {
                minval = arr[j];
                minind = j;
            }
        }
        arr[minind] = arr[i];
        arr[i] = minval;
    }
}
fn main() {
    let n = 30000;
    let mut arr = (0..n).map(|_| rand::random_range(0..n)).collect();

    // an unbiased integer over the entire range:

    let start = Instant::now();
    selection_sort(&mut arr);
    let dur = Instant::now() - start;
    println!("{:?}", arr);
    println!("{:?}", dur);
}
