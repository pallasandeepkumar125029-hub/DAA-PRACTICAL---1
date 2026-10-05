import time
import sys

def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    # m[i][j] will store minimum cost of multiplying Ai...Aj
    m = [[0 for _ in range(n)] for _ in range(n)]

    # s[i][j] will store the index at which the optimal split occurs
    s = [[0 for _ in range(n)] for _ in range(n)]

    # L is chain length
    for L in range(2, n + 1):
        for i in range(0, n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        return f"A{i+1}"
    else:
        return "(" + print_optimal_parens(s, i, s[i][j]) + " x " + print_optimal_parens(s, s[i][j] + 1, j) + ")"


# --- User Input Section ---
if __name__ == "__main__":
    user_input = input("Enter matrix dimensions separated by spaces (e.g., for matrices A1(10x20), A2(20x30), A3(30x40), enter: 10 20 30 40): ")

    try:
        p = [int(x) for x in user_input.split()]

        print("\nMatrix dimensions:", p)

        # Record start time
        start_time = time.perf_counter()

        # Run Matrix Chain Order DP
        m, s = matrix_chain_order(p)

        # Record end time
        end_time = time.perf_counter()

        # Calculate execution time
        execution_time = end_time - start_time

        # Print Results
        print("Minimum number of multiplications:", m[0][len(p) - 2])
        print("Optimal Parenthesization:", print_optimal_parens(s, 0, len(p) - 2))
        print(f"Execution Time: {execution_time:.6f} seconds")

        # --- Time Complexity Info ---
        print("\n--- Time Complexity Analysis ---")
        print("Best Case: O(n³)")
        print("Worst Case: O(n³)")
        print("Average Case: O(n³)")

    except ValueError:
        print("Please enter valid integers separated by spaces.")
