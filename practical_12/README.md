# Practical 12: Travelling Salesman Problem (TSP)

## 1. Aim
To implement and analyze the **Travelling Salesman Problem (TSP)** to find the minimum-cost Hamiltonian cycle using the **Held-Karp Dynamic Programming algorithm**.

---

## 2. Overview & Problem Statement

The **Travelling Salesman Problem (TSP)** is one of the most famous and foundational problems in computer science and operations research. 

### The Problem in Simple Words:
A salesperson must visit a given set of $n$ cities:
1. They must start at a specific home city (e.g., City 0).
2. They must visit every other city **exactly once**.
3. They must return back to their starting home city.
4. The goal is to minimize the **total travel distance, time, or cost**.

Mathematically, this corresponds to finding a **minimum-weight Hamiltonian cycle** in a weighted, complete graph.

---

## 3. Algorithmic Approaches

| Approach | Method | Time Complexity | Feasibility |
| :--- | :--- | :--- | :--- |
| **Brute Force** | Evaluate all $(n-1)!$ permutations of tours | $O(n!)$ | Unusable for $n > 12$ ($10! \approx 3.6$ million) |
| **Backtracking / Branch & Bound** | Explore state space tree with cost-bound pruning | $O(n!)$ worst-case | Faster average case, but still exponential |
| **Held-Karp (Dynamic Programming)** | Reuses sub-tour costs using bitmasks | $O(n^2 \cdot 2^n)$ | Optimal and exact for $n \le 20$ |

### The Held-Karp Dynamic Programming Principle:
Instead of trying every permutation from scratch, notice an overlapping subproblem:
If you are currently at City $u$ having already visited a subset of cities $S$, you don't need to care in what order you visited the cities in $S$—you only care about the **minimum cost** to have visited them and what cities remain!

#### Recurrence Relation:
Let `cost(S, u)` denote the minimum cost to visit all cities in subset $S$, starting from City 0 and currently standing at City $u$:

$$\text{cost}(S, u) = \min_{v \notin S} \left\{ \text{dist}[u][v] + \text{cost}(S \cup \{v\}, v) \right\}$$

- **Base Case:** When all cities have been visited ($S = \{0, 1, \dots, n-1\}$), the cost to complete the cycle is simply the direct distance back to the starting city: $\text{dist}[u][0]$.
- **Bitmask Representation:** We represent the subset of visited cities as an integer bitmask, where the $i$-th bit is $1$ if City $i$ is visited, and $0$ otherwise.

---

## 4. Source Code and Execution

- **Source File:** [`travelling_salesman.py`](file:///c:/Users/Sandeep%20Kumar/OneDrive/Desktop/DAA_lab/practical_12/travelling_salesman.py)

### How to Run:
```bash
python practical_12/travelling_salesman.py
```

### Sample Cost Matrix (4 Cities):
```
          City 0     City 1     City 2     City 3     
------------------------------------------------------
City 0    | 0          10         15         20         
City 1    | 10         0          35         25         
City 2    | 15         35         0          30         
City 3    | 20         25         30         0          
```

### Execution Output:
```
=================================================================
Practical 12: Travelling Salesman Problem (Held-Karp DP)
=================================================================

Distance / Cost Matrix between Cities:
          City 0     City 1     City 2     City 3     
------------------------------------------------------
City 0    | 0          10         15         20         
City 1    | 10         0          35         25         
City 2    | 15         35         0          30         
City 3    | 20         25         30         0          

Solving for the optimal Hamiltonian tour starting & ending at City 0...

Optimal Tour Route:
  City 0 -> City 1 -> City 3 -> City 2 -> City 0

Minimum Tour Cost: 80

Trip Breakdown (Leg by Leg):
---------------------------------------------
  Leg 1: City 0 -> City 1 | Cost = 10 (Cumulative = 10)
  Leg 2: City 1 -> City 3 | Cost = 25 (Cumulative = 35)
  Leg 3: City 3 -> City 2 | Cost = 30 (Cumulative = 65)
  Leg 4: City 2 -> City 0 | Cost = 15 (Cumulative = 80)
---------------------------------------------

Execution Time: ~0.000053 seconds
```

---

## 5. Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n^2 \cdot 2^n)$ | There are $2^n$ possible subsets of visited cities, and for each subset, $n$ possible endpoints. Transition checks take $O(n)$. |
| **Space Complexity** | $O(n \cdot 2^n)$ | Memoization table stores solutions for $(2^n \times n)$ distinct subproblem states. |

---

## 6. Summary (Simple & Humanized)

Imagine you are a delivery driver or courier tasked with delivering packages across four or five different neighborhoods and then heading back home. 

If you try to figure out the best route by writing down every single possible route on paper (the brute-force way), you'll quickly get overwhelmed. For just 10 locations, there are over 180,000 routes; for 20 locations, there are more combinations than seconds since the universe began!

The **Held-Karp algorithm** saves us with a much smarter human intuition: **"Don't reinvent the wheel."** 
If you are standing in Neighborhood B and have already dropped off parcels in Neighborhoods A and C, it doesn't matter what sequence you did them in. All you need to remember is the cheapest way you reached Neighborhood B, and then focus on finding the best path forward to the remaining unvisited locations. By remembering and reusing these sub-journey costs instead of recalculating them, Dynamic Programming cuts the search down from impossible factorial time to manageable exponential time.

---

## 7. Conclusion (Simple & Humanized)

The Travelling Salesman Problem is the ultimate rite of passage in algorithm study. It opens the door to understanding **NP-Hard** problems—problems so inherently complex that no magical shortcut exists to solve them in polynomial time for massive scales.

However, implementing Held-Karp proves that we aren't helpless against hard problems. By combining **Dynamic Programming** with **bitmasking**, we turn an intractable $O(n!)$ search into an exact $O(n^2 \cdot 2^n)$ solution that easily handles small-to-moderate logistical challenges. For everyday real-world applications with thousands of destinations—like delivery logistics (Amazon, FedEx), flight scheduling, and microchip drilling—engineers take these exact insights and build fast approximation heuristics. This practical gives us a deep appreciation for the trade-off between computational cost and solution optimality.
