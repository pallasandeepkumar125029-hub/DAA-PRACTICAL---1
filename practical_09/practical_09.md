# Practical 9: Implementation of Prim's Algorithm

## Summary

Prim's Algorithm is a greedy algorithm that finds a Minimum Spanning Tree (MST) for a weighted undirected graph. A Minimum Spanning Tree connects all the vertices in the graph with the minimum possible total edge weight, without forming any cycles.

## Working Principle

1. Initialize a tree with a single arbitrarily chosen starting vertex.
2. Grow the tree by one edge at a time: find the minimum-weight edge that connects a vertex inside the tree to a vertex outside the tree.
3. Add the edge and the new vertex to the tree.
4. Repeat step 2 until all vertices are included in the MST.

## Files

- [`prims.py`](file:///c:/Users/Sandeep%20Kumar/OneDrive/Desktop/DAA_lab/practical_09/prims.py): Python implementation of Prim's Algorithm using an adjacency matrix representation.
