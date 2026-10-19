# Practical 11: All-Pairs Shortest Path using Floyd-Warshall Algorithm

## Summary

The Floyd-Warshall Algorithm is a dynamic programming algorithm used to find the shortest paths between all pairs of vertices in a weighted, directed or undirected graph. It also works with negative edge weights as long as there are no negative weight cycles.

The algorithm systematically considers each vertex as an intermediate transit point and updates the path cost between every pair of vertices $(i, j)$ using the relaxation rule:
$$D[i][j] = \min(D[i][j], D[i][k] + D[k][j])$$

## Complexity

- **Time Complexity**: $\Theta(V^3)$ for best, average, and worst cases due to three nested loops iterating over all vertices.
- **Space Complexity**: $O(V^2)$ to store the distance matrix and path reconstruction predecessor table.

## Conclusion

Floyd-Warshall is an elegant and powerful dynamic programming solution for all-pairs shortest paths on dense graphs. It provides complete distance information and path reconstruction for all vertex pairs in $O(V^3)$ time, while simultaneously offering straightforward negative cycle detection.
