import time

# Quick Sort Function
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

# Partition Function
def partition(arr, low, high):
    pivot = arr[high]      # Last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Swap
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

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
quick_sort(arr, 0, len(arr) - 1)

# End Timer
end_time = time.perf_counter()

execution_time = end_time - start_time

print("\nSorted List:", arr)

print(f"\nExecution Time: {execution_time:.10f} seconds")

print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n²)")

print("\nSpace Complexity:")
print("Average Case : O(log n)")
print("Worst Case   : O(n)")