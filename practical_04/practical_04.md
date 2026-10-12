# Practical 4: Factorial Using Iteration and Recursion

## Summary

The factorial of a non-negative integer `n` is the product of all positive integers from `1` to `n`. It is written as `n!`. By definition, `0!` is equal to `1`.

### Iterative Method

The iterative method calculates the factorial using a loop. It starts with a result of `1` and repeatedly multiplies the result by each number from `1` to `n`.

### Recursive Method

The recursive method defines the factorial in terms of a smaller factorial:

`n! = n * (n - 1)!`

The recursion stops at the base case when `n` is `0` or `1`, returning `1`.

## Complexity

Both methods have a time complexity of `O(n)`. The iterative method uses `O(1)` additional space, while the recursive method uses `O(n)` space because of the function call stack.

## Conclusion

This practical demonstrates two ways to solve the factorial problem. The iterative approach uses less memory, while the recursive approach is shorter and clearly shows the mathematical definition of factorial.
