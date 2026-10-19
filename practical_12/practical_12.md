# Practical 12: Travelling Salesman Problem using Dynamic Programming

## Summary

The Travelling Salesman Problem (TSP) seeks the shortest possible tour that visits each city exactly once and returns to the original departure city. It is a classic NP-hard combinatorial optimization problem.

This implementation uses the Held-Karp Dynamic Programming algorithm with bitmasking. By representing visited cities as bit flags, the algorithm breaks down the problem into smaller overlapping subproblems:
$$\text{cost}(S, u) = \min_{v \notin S} (\text{dist}[u][v] + \text{cost}(S \cup \{v\}, v))$$
This avoids redundant calculations and computes the exact optimal Hamiltonian tour along with a step-by-step path reconstruction.

## Complexity

- **Time Complexity**: $O(n^2 \cdot 2^n)$, representing an exponential improvement over the brute-force factorial complexity $O(n!)$.
- **Space Complexity**: $O(n \cdot 2^n)$ to store intermediate optimal sub-tour states in the memoization table.

## Conclusion

Solving the Travelling Salesman Problem with Dynamic Programming illustrates how memoization and state compression tame combinatorial explosions. While TSP remains computationally intractable for very large datasets, the Held-Karp algorithm guarantees an exact, globally optimal tour for small-to-moderate networks, serving as the benchmark for real-world approximation and heuristic routing systems.
