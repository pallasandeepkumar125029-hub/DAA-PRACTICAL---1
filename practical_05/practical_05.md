# Practical 5: 0/1 Knapsack Problem using Dynamic Programming

## Summary

The 0/1 Knapsack problem involves selecting a subset of items, each having a weight and a value, such that the total weight does not exceed the knapsack capacity and the total value is maximized.

The program uses Dynamic Programming (DP) by constructing a 2D table `dp[n+1][W+1]`, where `dp[i][w]` represents the maximum value achievable using a subset of the first `i` items with a maximum weight capacity `w`.

## Complexity

- **Time Complexity**: `O(n * W)`, where `n` is the number of items and `W` is the knapsack capacity.
- **Space Complexity**: `O(n * W)` for storing the DP table.

## Conclusion

Dynamic Programming provides an optimal solution to the 0/1 Knapsack problem by solving subproblems bottom-up and avoiding repetitive computations.
