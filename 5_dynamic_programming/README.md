# Dynamic Programming

## [LeetCode Problems](./leetcode/)

## History

- Richard Bellman 1950s
- Not actually dynamic, programming meant something else then
- Recursion without repitition

## Top Down Memoization

- Use a hashmap to store values during recursion to prevent repetitions
- Just use stored result when calling recursion with the same values
- Typically store into variable named `memorandum/memo`
- Fib example

```
def fib(n):
    if n in memo:
        return memo[n]
    if n==0 or n==1: return n
    else:
        memo[n]=fib(n-1)+fib(n-2)
```
