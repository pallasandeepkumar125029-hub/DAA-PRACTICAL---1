# Practical 11: Floyd-Warshall Algorithm for All-Pairs Shortest Paths (APSP)
# Design and Analysis of Algorithms (DAA)

import time

INF = float('inf')


def floyd_warshall(graph, num_vertices):
    """
    Computes shortest distances between all pairs of vertices
    using the Floyd-Warshall dynamic programming algorithm.

    Parameters:
        graph: 2D adjacency matrix (INF represents no direct edge)
        num_vertices: Total number of vertices

    Returns:
        dist: 2D matrix of shortest path distances
        next_node: 2D matrix for path reconstruction
        has_negative_cycle: Boolean indicating presence of negative cycle
    """
    # Initialize distance matrix with graph values
    dist = [[graph[i][j] for j in range(num_vertices)] for i in range(num_vertices)]

    # Initialize next_node matrix for path reconstruction
    next_node = [[None for _ in range(num_vertices)] for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and dist[i][j] != INF:
                next_node[i][j] = j

    # Main Floyd-Warshall DP step:
    # Consider each vertex k as an intermediate point
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]

    # Check for negative-weight cycles
    has_negative_cycle = False
    for i in range(num_vertices):
        if dist[i][i] < 0:
            has_negative_cycle = True
            break

    return dist, next_node, has_negative_cycle


def reconstruct_path(u, v, next_node):
    """Reconstructs the shortest path from vertex u to vertex v."""
    if next_node[u][v] is None:
        return []
    path = [u]
    curr = u
    while curr != v:
        curr = next_node[curr][v]
        path.append(curr)
    return path


def print_matrix(matrix, num_vertices, title="Matrix:"):
    """Helper function to print 2D distance matrix formatted cleanly."""
    print(title)
    header = "       " + "".join(f"V{j:<8}" for j in range(num_vertices))
    print(header)
    print("-" * len(header))
    for i in range(num_vertices):
        row = f"V{i:<5} | "
        for j in range(num_vertices):
            val = matrix[i][j]
            if val == INF:
                row += f"{'INF':<8}"
            else:
                row += f"{val:<8}"
        print(row)
    print()


def main():
    print("=" * 65)
    print("Practical 11: Floyd-Warshall Algorithm (All-Pairs Shortest Path)")
    print("=" * 65)

    # Sample Graph representation (Adjacency Matrix)
    # INF indicates no direct edge exists
    sample_graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]
    num_vertices = 4

    print("\nInitial Cost Adjacency Matrix:")
    print_matrix(sample_graph, num_vertices, title="Input Graph:")

    # Measure algorithm execution time
    start_time = time.perf_counter()
    dist, next_node, has_negative_cycle = floyd_warshall(sample_graph, num_vertices)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    if has_negative_cycle:
        print("Warning: The graph contains a negative-weight cycle! Shortest paths are undefined.")
    else:
        print_matrix(dist, num_vertices, title="Final All-Pairs Shortest Distance Matrix:")

        print("Shortest Paths between Distinct Vertices:")
        print("-" * 50)
        for i in range(num_vertices):
            for j in range(num_vertices):
                if i != j:
                    path = reconstruct_path(i, j, next_node)
                    if path:
                        path_str = " -> ".join(f"V{node}" for node in path)
                        print(f"Path from V{i} to V{j}: {path_str} (Cost: {dist[i][j]})")
                    else:
                        print(f"Path from V{i} to V{j}: No Path exists (Cost: INF)")
        print("-" * 50)

    print(f"\nExecution Time: {execution_time:.8f} seconds")

    # Time and Space Complexity Analysis
    print("\n" + "=" * 35)
    print("    COMPLEXITY ANALYSIS")
    print("=" * 35)
    print("Time Complexity:")
    print("  - Best Case    : O(V^3)")
    print("  - Average Case : O(V^3)")
    print("  - Worst Case   : O(V^3)")
    print("\nSpace Complexity:")
    print("  - O(V^2) for distance and path reconstruction matrices")
    print("=" * 35)


if __name__ == "__main__":
    main()
