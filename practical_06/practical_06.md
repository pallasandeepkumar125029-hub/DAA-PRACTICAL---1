# Practical 6: Matrix Chain Multiplication using Dynamic Programming

## Summary

Matrix Chain Multiplication determines the most efficient way to multiply a given sequence of matrices. The goal is to find the order of multiplications that minimizes the total number of scalar multiplications required.

The algorithm uses Dynamic Programming by building a table `m[n][n]` where `m[i][j]` represents the minimum scalar multiplications needed to compute matrix product `Ai...Aj`.

## Complexity

- **Time Complexity**: `O(n³)` where `n` is the number of matrices.
- **Space Complexity**: `O(n²)` for storing split table and cost matrix.

## Conclusion

Dynamic Programming optimizes matrix chain multiplication by solving smaller sub-chain problems first, reducing computational effort compared to brute-force parenthesization.
