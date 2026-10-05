import time

# Selection Sort Function
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        # Find the minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# User Input
n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

print("\nOriginal List:", arr)

# Start Timer
start_time = time.perf_counter()

# Sorting
selection_sort(arr)

# End Timer
end_time = time.perf_counter()

execution_time = end_time - start_time

print("\nSorted List:", arr)

print(f"\nExecution Time: {execution_time:.10f} seconds")

print("\nTime Complexity:")
print("Best Case    : O(n²)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")

print("\nSpace Complexity:")
print("O(1)")