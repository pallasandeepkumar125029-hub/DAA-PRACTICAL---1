# Practical 7: Coin Change Using Dynamic Programming

## Summary

The coin change problem finds the minimum number of coins required to make a given amount. The program accepts a list of coin denominations and an amount, then uses dynamic programming to calculate the best solution.

The algorithm builds a table where each position stores the minimum number of coins needed to create that amount. It starts with `minimum[0] = 0` and calculates each larger amount using the previously solved smaller amounts. A second list stores the last coin used, allowing the program to reconstruct and display one optimal combination.

For example, with coins `1, 2, 5` and amount `11`, the minimum number of coins is `3`, using `[1, 5, 5]`. If the amount cannot be formed, the program displays an appropriate message.

## Complexity

If there are `n` coin denominations and the target amount is `A`, the time complexity is `O(nA)` and the space complexity is `O(A)`.

## Conclusion

Dynamic programming solves the coin change problem efficiently by storing solutions to smaller amounts and reusing them. This avoids recalculating the same subproblems and guarantees the minimum number of coins for the given denominations.
