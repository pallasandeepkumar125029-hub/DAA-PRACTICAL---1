# Practical 11: Implementation of Floyd-Warshall Algorithm

## 1. Aim
To implement and analyze the **Floyd-Warshall Algorithm** for solving the **All-Pairs Shortest Path (APSP)** problem in a weighted directed/undirected graph using Dynamic Programming.

---

## 2. Overview & Working Principle

The **Floyd-Warshall Algorithm** finds the shortest distance between every pair of vertices in a given weighted graph. Unlike single-source algorithms (such as Dijkstra's or Bellman-Ford), Floyd-Warshall produces a complete matrix containing the shortest paths between all pairs $(u, v)$ in a single algorithm run. It can handle positive and negative edge weights, provided there are no negative-weight cycles.

### Intuition (The Core Idea)
Imagine you are planning road trips between multiple cities. Rather than recalculating routes from scratch, you ask one simple question repeatedly:
> *"If I allow a detour through City $k$, is it faster to go from City $i$ to City $j$ via $k$ compared to my direct route?"*

By systematically testing every city $k \in \{0, 1, \dots, V-1\}$ as a possible intermediate stop for all pairs $(i, j)$, you progressively uncover the shortest possible journeys.

### Recurrence Relation
At step $k$, the shortest distance from vertex $i$ to vertex $j$ using intermediate vertices chosen from $\{0, 1, \dots, k\}$ is given by:

$$D^{(k)}[i][j] = \min \left( D^{(k-1)}[i][j], \; D^{(k-1)}[i][k] + D^{(k-1)}[k][j] \right)$$

- **Base Case ($k = 0$):** $D^{(0)}[i][j]$ is initialized with the direct edge weight from $i$ to $j$, $0$ if $i = j$, and $\infty$ (INF) if no direct edge exists.
- **Negative Cycle Detection:** If any diagonal value $D[i][i] < 0$ after all iterations, the graph contains a negative-weight cycle.

---

## 3. Algorithm Steps

1. **Initialization:**
   - Create a 2D distance matrix `dist` initialized with edge weights from the input graph.
   - Set diagonal elements `dist[i][i] = 0`.
   - Set `dist[i][j] = INF` where no direct edge exists.
   - Initialize a predecessor/next-node matrix `next_node` to reconstruct actual routes.
2. **Three Nested Loops:**
   - Outer loop picks intermediate vertex `k` from $0$ to $V-1$.
   - Middle loop picks source vertex `i` from $0$ to $V-1$.
   - Inner loop picks destination vertex `j` from $0$ to $V-1$.
3. **Relaxation:**
   - If `dist[i][k] + dist[k][j] < dist[i][j]`, update `dist[i][j]` with the shorter path and record `next_node[i][j] = next_node[i][k]`.
4. **Validation:**
   - Verify if any `dist[i][i] < 0` to identify negative-weight cycles.
5. **Output:**
   - Print the final all-pairs distance table and reconstruct paths between vertices.

---

## 4. Source Code and Execution

- **Source File:** [`floyd_warshall.py`](file:///c:/Users/Sandeep%20Kumar/OneDrive/Desktop/DAA_lab/practical_11/floyd_warshall.py)

### How to Run:
```bash
python practical_11/floyd_warshall.py
```

### Sample Input Graph:
```
Vertices: 4 (V0, V1, V2, V3)

Adjacency Matrix:
       V0       V1       V2       V3       
-------------------------------------------
V0     | 0       5       INF     10      
V1     | INF     0       3       INF     
V2     | INF     INF     0       1       
V3     | INF     INF     INF     0       
```

### Execution Output:
```
=================================================================
Practical 11: Floyd-Warshall Algorithm (All-Pairs Shortest Path)
=================================================================

Initial Cost Adjacency Matrix:
Input Graph:
       V0       V1       V2       V3       
-------------------------------------------
V0     | 0       5       INF     10      
V1     | INF     0       3       INF     
V2     | INF     INF     0       1       
V3     | INF     INF     INF     0       

Final All-Pairs Shortest Distance Matrix:
       V0       V1       V2       V3       
-------------------------------------------
V0     | 0       5       8       9       
V1     | INF     0       3       4       
V2     | INF     INF     0       1       
V3     | INF     INF     INF     0       

Shortest Paths between Distinct Vertices:
--------------------------------------------------
Path from V0 to V1: V0 -> V1 (Cost: 5)
Path from V0 to V2: V0 -> V1 -> V2 (Cost: 8)
Path from V0 to V3: V0 -> V1 -> V2 -> V3 (Cost: 9)
Path from V1 to V0: No Path exists (Cost: INF)
Path from V1 to V2: V1 -> V2 (Cost: 3)
Path from V1 to V3: V1 -> V2 -> V3 (Cost: 4)
Path from V2 to V0: No Path exists (Cost: INF)
Path from V2 to V1: No Path exists (Cost: INF)
Path from V2 to V3: V2 -> V3 (Cost: 1)
Path from V3 to V0: No Path exists (Cost: INF)
Path from V3 to V1: No Path exists (Cost: INF)
Path from V3 to V2: No Path exists (Cost: INF)
--------------------------------------------------

Execution Time: ~0.000021 seconds
```

---

## 5. Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Best Case Time** | $O(V^3)$ | Three nested loops always execute $V \times V \times V$ times. |
| **Average Case Time** | $O(V^3)$ | Every triplet $(k, i, j)$ is checked uniformly. |
| **Worst Case Time** | $O(V^3)$ | Constant number of operations per triplet iteration. |
| **Space Complexity** | $O(V^2)$ | Requires a $V \times V$ 2D matrix for distances and path tracking. |

---

## 6. Summary (Simple & Humanized)

At its heart, the **Floyd-Warshall algorithm** is all about finding shortcuts. 

Think of it like an everyday GPS or transit map where you want to know the travel time between every single stop in the city. Instead of trying to guess complex combinations all at once, Floyd-Warshall takes a calm, organized approach: it tests one station at a time as a possible transfer point. 

First, it asks: *"Does changing trains at Station 0 make any journey faster?"* Then it asks the same for Station 1, Station 2, and so forth. By the time it has checked all stations as potential pitstops, you are guaranteed to have the absolute fastest route between any two points on the map. It's clean, elegant, and avoids repetitive guesswork by building directly on top of solutions found in previous steps.

---

## 7. Conclusion (Simple & Humanized)

Floyd-Warshall demonstrates the real beauty of **Dynamic Programming**: taking a problem that feels overwhelming and solving it with just three clean nested loops.

While its $O(V^3)$ runtime makes it a bit heavy for massive road networks with millions of intersections, it is the undisputed champion for moderate-sized, dense networks. You get answers for every single pair in one single shot, easily detect dangerous negative-cost loops, and gain an intuitive way to trace the exact turn-by-turn path. It is a fundamental algorithm that teaches us how small, incremental checks lead to globally optimal solutions.
