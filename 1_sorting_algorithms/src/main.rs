use sorting_algos::{
    algos::{heapsort, hoare_quicksort, lumoto_quicksort},
    mergesort, run_algo,
};

fn main() {
    println!("Comparing functions.");
    let n = 50000;
    let arr: Vec<i32> = (0..n).map(|_| rand::random_range(0..n)).collect();
    run_algo(heapsort, &arr);
    run_algo(hoare_quicksort, &arr);
    run_algo(lumoto_quicksort, &arr);
    run_algo(mergesort, &arr);
}
