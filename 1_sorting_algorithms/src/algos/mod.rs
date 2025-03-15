mod bubblesort;
mod countingsort;
mod heapsort;
mod hoare_quicksort;
mod insertionsort;
mod lumoto_quicksort;
mod mergesort;
mod radixsort;
mod selectionsort;

use std::{fmt, time::Duration};

use bubblesort::bubble_sort;
use countingsort::countingsort;
use heapsort::heapsort;
use hoare_quicksort::hoare_quicksort;
use indicatif::{ProgressBar, ProgressStyle};
use insertionsort::insertion_sort;
use lumoto_quicksort::lumoto_quicksort;
use mergesort::mergesort;
use radixsort::radixsort;
use selectionsort::selectionsort;
use serde::Serialize;
use strum_macros::EnumIter;

fn sort(arr: &mut Vec<i32>) {
    arr.sort();
}

fn sort_unstable(arr: &mut Vec<i32>) {
    arr.sort_unstable();
}

#[derive(Debug, EnumIter, Clone, Serialize, clap::ValueEnum)]
#[serde(rename_all = "lowercase")]
pub enum SortingAlgo {
    Bubble,
    Counting,
    Heap,
    Hoare,
    Lumoto,
    Merge,
    Selection,
    Insertion,
    Stable,
    Unstable,
    Radix,
}

impl fmt::Display for SortingAlgo {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "{}",
            serde_json::to_string(self).unwrap().replace("\"", "")
        )
    }
}

impl SortingAlgo {
    pub fn algo(&self) -> impl Fn(&mut Vec<i32>) {
        match self {
            Self::Bubble => bubble_sort,
            Self::Counting => countingsort,
            Self::Heap => heapsort,
            Self::Hoare => hoare_quicksort,
            Self::Lumoto => lumoto_quicksort,
            Self::Merge => mergesort,
            Self::Selection => selectionsort,
            Self::Insertion => insertion_sort,
            Self::Stable => sort,
            Self::Unstable => sort_unstable,
            Self::Radix => radixsort,
        }
    }

    fn is_enabled(&self) -> bool {
        let key = self.to_string().to_uppercase();
        std::env::var(key).is_ok()
    }

    pub fn run(&self, arr: &Vec<i32>) {
        if !self.is_enabled() {
            return;
        }
        let f = self.algo();
        let mut arr = arr.clone();
        let pb = ProgressBar::new_spinner();
        let template = format!("{} Running {} algo", "{spinner}", &self);
        let style = ProgressStyle::with_template(&template).unwrap();
        pb.set_style(style);
        pb.enable_steady_tick(Duration::from_millis(100));
        let start = std::time::Instant::now();
        f(&mut arr);
        let dur = std::time::Instant::now() - start;
        pb.finish_and_clear();
        println!("{} {:?}", &self, dur);
    }

    pub fn debug(&self, arr: &mut Vec<i32>) {
        let f = self.algo();
        println!("{:?}\n", &arr);
        let start = std::time::Instant::now();
        f(arr);
        let dur = std::time::Instant::now() - start;
        println!("{} {:?}", self, dur);
        println!("{:?}", &arr[..5]);
    }
}
