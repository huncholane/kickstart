use std::time::Instant;

pub mod algos;
pub use algos::*;

pub fn debug_algo<F>(f: F, n: i32)
where
    F: Fn(&mut Vec<i32>),
{
    let mut arr: Vec<i32> = (0..n).map(|_| rand::random_range(0..n)).collect();
    let start = std::time::Instant::now();
    f(&mut arr);
    let dur = std::time::Instant::now() - start;
    println!("{} {:?}", std::any::type_name::<F>(), dur);
    println!("{:?}", &arr[..5]);
}
