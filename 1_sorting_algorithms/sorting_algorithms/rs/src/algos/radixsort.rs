pub fn radixsort(arr: &mut Vec<i32>) {
    let (mut low, mut high) = (arr[0], arr[1]);
    let n = arr.len();
    for i in 0..n {
        if arr[i] < low {
            low = arr[i];
        } else if arr[i] > high {
            high = arr[i];
        }
    }
    for i in 0..n {
        arr[i] -= low;
    }
    let mut exp = 1;
    while high / exp > 0 {
        let mut output = vec![0; n];
        let mut count = vec![0; 10];

        for i in 0..n {
            let index = (arr[i] / exp) % 10;
            count[index as usize] += 1;
        }

        for i in 1..10 {
            count[i] += count[i - 1];
        }

        for i in (0..n).rev() {
            let index = (arr[i] / exp) % 10;
            let index = index as usize;
            output[count[index] - 1] = arr[i];
            count[index] -= 1;
        }

        for i in 0..n {
            arr[i] = output[i];
        }

        exp *= 10;
    }
    for i in 0..n {
        arr[i] += low;
    }
}
