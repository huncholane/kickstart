use std::time::Duration;

use clap::{ArgAction, Parser};
use indicatif::{ProgressBar, ProgressStyle};
use sorting_algos::SortingAlgo;
use strum::IntoEnumIterator;

/// Compares algorithms
#[derive(Parser, Debug)]
struct Args {
    /// How long is the array to sort?
    /// Defaults to env DEFAULT_TEST_N or 50000 if algo is not present.
    /// Defaults to env DEFAULT_DEBUG_N or 5 if algo is present.
    #[arg(short)]
    n: Option<usize>,

    /// What is the left of random numbers?
    /// Defaults to env DEFAULT_LEFT or 0.
    #[arg(short)]
    left: Option<i32>,

    /// What is the right of the random numbers?
    /// Defaults to env DEFAULT_RIGHT or n.
    #[arg(short)]
    right: Option<i32>,

    /// Want to debug an algo?
    /// Debugs specific algo if present.
    /// Tests all algos enabled with env if not present.
    #[arg(short, action = ArgAction::Set,value_enum)]
    algo: Option<SortingAlgo>,
}

fn main() {
    let args = Args::parse();
    let n: usize = match args.n {
        Some(n) => n,
        _ => match args.algo.is_some() {
            true => match option_env!("DEFAULT_DEBUG_N") {
                Some(n) => n.parse().expect("Expected integer for DEFAULT_DEBUG_N"),
                _ => 5,
            },
            _ => match option_env!("DEFAULT_TEST_N") {
                Some(n) => n.parse().expect("Expected integer for DEFAULT_TEST_N"),
                _ => 50000,
            },
        },
    };
    let l: i32 = match args.left {
        Some(l) => l,
        _ => match option_env!("DEFAULT_LEFT") {
            Some(l) => l.parse().expect("Expected an integer for DEFAULT_LEFT"),
            _ => 0,
        },
    };
    let r: i32 = match args.right {
        Some(r) => r,
        _ => match option_env!("DEFAULT_RIGHT") {
            Some(r) => r.parse().expect("Expected an integer for DEFAULT_RIGHT"),
            _ => n as i32,
        },
    };
    let pb = ProgressBar::new_spinner();
    let style = ProgressStyle::with_template("{spinner} Loading Random Numbers").unwrap();
    pb.set_style(style);
    pb.enable_steady_tick(Duration::from_millis(100));
    let mut arr: Vec<i32> = (0..n).map(|_| rand::random_range(l..r)).collect();
    pb.finish_and_clear();
    println!("n={}, l={}, r={}", n, l, r);
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
