use std::time::Instant;

use sorting_algos::algos::lumoto_quicksort;

fn main() {
    let n = 50000;
    let mut arr: Vec<i32> = (0..n).map(|_| rand::random_range(0..n)).collect();

    let start = Instant::now();
    lumoto_quicksort(&mut arr);
    let dur = Instant::now() - start;
    println!("{:?}", dur);
    println!("{:?}", &arr[..5]);
}
