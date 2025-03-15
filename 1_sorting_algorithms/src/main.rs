use std::{str::FromStr, time::Duration};

use clap::Parser;
use indicatif::{ProgressBar, ProgressStyle};
use sorting_algos::SortingAlgo;
use strum::IntoEnumIterator;

/// Compares algorithms
#[derive(Parser, Debug)]
struct Args {
    /// How long is the array to sort?
    #[arg(short)]
    n: Option<usize>,

    /// What is the range of random numbers?
    #[arg(short)]
    k: Option<i32>,

    /// Select specific algo
    #[arg(short)]
    algo: Option<SortingAlgo>,
}

fn main() {
    let args = Args::parse();
    let n = match args.n {
        Some(n) => n,
        _ => 50000,
    };
    let k = match args.k {
        Some(k) => k,
        _ => n as i32,
    };
    let pb = ProgressBar::new_spinner();
    let style = ProgressStyle::with_template("{spinner} Loading Random numbers").unwrap();
    pb.set_style(style);
    pb.enable_steady_tick(Duration::from_millis(100));
    let mut arr: Vec<i32> = (0..n).map(|_| rand::random_range(0..k)).collect();
    pb.finish_and_clear();
    println!("n={}, k={}", n, k);
    if let Some(algo) = args.algo {
        println!("Debugging {}", algo);
        algo.debug(&mut arr);
    } else {
        println!("Comparing functions.");
        for algo in SortingAlgo::iter() {
            algo.run(&arr);
        }
    }
}
