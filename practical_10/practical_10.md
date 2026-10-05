# Practical 10: Implementation of Kruskal's Algorithm

## Summary

Kruskal's Algorithm is a greedy algorithm used to find a Minimum Spanning Tree (MST) for a connected, weighted graph. It finds a subset of edges that forms a tree including every vertex, where the total weight of all edges in the tree is minimized.

## Working Principle

1. Sort all edges of the graph in non-decreasing order of their weight.
2. Pick the edge with the smallest weight.
3. Check if adding the edge forms a cycle with the spanning tree formed so far (using Disjoint Set Union / Union-Find data structure).
4. If a cycle is not formed, include the edge in the MST. Otherwise, discard it.
5. Repeat steps 2-4 until there are \((V - 1)\) edges in the MST (where \(V\) is the number of vertices).


