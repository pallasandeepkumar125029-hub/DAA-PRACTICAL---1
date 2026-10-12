import time

# 0/1 Knapsack Function using Dynamic Programming
def knapsack(weights, values, capacity, n):
    # Create DP table initialized with 0
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Maximum profit achieved
    max_value = dp[n][capacity]

    # Trace back to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)  # Item index (1-based)
            w -= weights[i - 1]

    selected_items.reverse()
    return max_value, selected_items

# User Input
n = int(input("Enter the number of items: "))

weights = []
values = []

print("\nEnter the weight and value for each item:")
for i in range(n):
    w = int(input(f"Enter weight of item {i + 1}: "))
    v = int(input(f"Enter value of item {i + 1}: "))
    weights.append(w)
    values.append(v)

capacity = int(input("\nEnter the maximum capacity of the knapsack: "))

print("\nOriginal Weights  :", weights)
print("Original Values   :", values)
print("Knapsack Capacity :", capacity)

# Start Timer
start_time = time.perf_counter()

# Dynamic Programming Knapsack Calculation
max_value, selected_items = knapsack(weights, values, capacity, n)

# End Timer
end_time = time.perf_counter()

execution_time = end_time - start_time

# Output Results
print("\nMaximum Profit / Value:", max_value)
print("Selected Items (1-indexed):", selected_items)

print(f"\nExecution Time: {execution_time:.10f} seconds")

print("\nTime Complexity:")
print("Best Case    : O(n * W)")
print("Average Case : O(n * W)")
print("Worst Case   : O(n * W)")

print("\nSpace Complexity:")
print("O(n * W)")
