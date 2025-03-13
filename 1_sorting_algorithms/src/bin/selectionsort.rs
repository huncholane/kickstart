use std::time::Instant;

use sorting_algos::selection_sort;

fn main() {
    let n = 50000;
    let mut arr = (0..n).map(|_| rand::random_range(0..n)).collect();

    // an unbiased integer over the entire range:

    let start = Instant::now();
    selection_sort(&mut arr);
    let dur = Instant::now() - start;
    println!("{:?}", dur);
    println!("{:?}", &arr[..5]);
}
