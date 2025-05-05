# [322. Coin Change]

- Return fewest number of coins to make an amount
- Minimization/optimization problem &rarr; dynamic programming

  - Greedy strategy will not work for example

  ```text
  options = [1,5,7], target = 10
  Greedy picks 7+1+1+1 and it should be 5+5
  ```

- Correct Solution with Dynamic Programming

1. Optimization Problem

2. Come up with a recurrence equation (hardest part)

   ```text
   c1+c2+c3+...+ck = a
   f(a) = fewest # coins to construct amount a.
   coins = [c1, c2, c3, ..., ck]
   f(a-c1)
   f(a-c2)
   ...
   f(a-ck)

   f(a) - min(f(a-ck))+1
   ```

   - determine **last** coin that would lead to amount a

3. Identify all the subproblems

   - a+1 distinct subproblems

4. Identify depencies
   - Each subproblem &rarr; vertex

5. Identify the data structure (usually a table)

6. Write up the DP algorithm
    ```text 
    def coinchange(a, coins):
        table = 1d array of size (a+1)
        # Base case
        table[0] = 0
        Initialize rest of the table to INF
        for i in 1 to a:
            # Compute and cache f(i)
            for c in coins:
                if i-c >= 0:
                    table[i] = min(table[i], table[i-c])
            table[i]++
        return table[a]
    ```

- T(a,k) = O(ak)
- S(a,k) = O(a)
