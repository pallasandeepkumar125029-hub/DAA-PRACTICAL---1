# Practical 12: Travelling Salesman Problem (TSP)
# Design and Analysis of Algorithms (DAA)

import time

INF = float('inf')


def tsp_held_karp(distance_matrix):
    """
    Solves the Travelling Salesman Problem to optimality using the
    Held-Karp algorithm (Dynamic Programming with Bitmasking).

    Parameters:
        distance_matrix: 2D list where distance_matrix[i][j] is the cost
                         to travel from city i to city j.

    Returns:
        min_cost: Minimum total tour cost
        tour: List of city indices in the optimal tour sequence (starts & ends at 0)
    """
    n = len(distance_matrix)
    # memo[(mask, u)] = (cost, path_from_u)
    # mask has bit i set if city i has been visited.
    memo = {}

    def solve(mask, u):
        # Base case: All cities have been visited
        if mask == (1 << n) - 1:
            # Return cost from the last city u back to starting city 0
            return distance_matrix[u][0], [0]

        state = (mask, u)
        if state in memo:
            return memo[state]

        min_cost = INF
        best_path = []

        for v in range(n):
            # If city v has not been visited yet
            if not (mask & (1 << v)):
                next_mask = mask | (1 << v)
                sub_cost, sub_path = solve(next_mask, v)
                cost = distance_matrix[u][v] + sub_cost
                if cost < min_cost:
                    min_cost = cost
                    best_path = [v] + sub_path

        memo[state] = (min_cost, best_path)
        return memo[state]

    # Start tour at city 0 with mask indicating city 0 is visited (1 << 0)
    min_cost, path_rest = solve(1 << 0, 0)
    tour = [0] + path_rest
    return min_cost, tour


def print_distance_matrix(matrix, num_cities):
    """Prints the cost/distance matrix between cities cleanly."""
    header = "          " + "".join(f"City {j:<6}" for j in range(num_cities))
    print(header)
    print("-" * len(header))
    for i in range(num_cities):
        row = f"City {i:<4} | "
        for j in range(num_cities):
            row += f"{matrix[i][j]:<11}"
        print(row)
    print()


def main():
    print("=" * 65)
    print("Practical 12: Travelling Salesman Problem (Held-Karp DP)")
    print("=" * 65)

    # Cost / Distance matrix between cities:
    # 4 cities example (Classic benchmark in DAA)
    cost_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    num_cities = len(cost_matrix)

    print("\nDistance / Cost Matrix between Cities:")
    print_distance_matrix(cost_matrix, num_cities)

    print("Solving for the optimal Hamiltonian tour starting & ending at City 0...\n")

    start_time = time.perf_counter()
    optimal_cost, optimal_tour = tsp_held_karp(cost_matrix)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Display Results
    tour_str = " -> ".join(f"City {c}" for c in optimal_tour)
    print("Optimal Tour Route:")
    print("  " + tour_str)
    print(f"\nMinimum Tour Cost: {optimal_cost}")

    # Detailed Tour Leg Breakdown
    print("\nTrip Breakdown (Leg by Leg):")
    print("-" * 45)
    leg_total = 0
    for i in range(len(optimal_tour) - 1):
        u = optimal_tour[i]
        v = optimal_tour[i + 1]
        step_cost = cost_matrix[u][v]
        leg_total += step_cost
        print(f"  Leg {i + 1}: City {u} -> City {v} | Cost = {step_cost} (Cumulative = {leg_total})")
    print("-" * 45)

    print(f"\nExecution Time: {execution_time:.8f} seconds")

    # Complexity Analysis
    print("\n" + "=" * 45)
    print("           COMPLEXITY ANALYSIS")
    print("=" * 45)
    print("Time Complexity:")
    print("  - Held-Karp DP  : O(n^2 * 2^n)")
    print("  - Brute Force   : O(n!)")
    print("  (Significantly faster than O(n!) for n <= 20)")
    print("\nSpace Complexity:")
    print("  - O(n * 2^n) to store DP memoization table")
    print("=" * 45)


if __name__ == "__main__":
    main()
