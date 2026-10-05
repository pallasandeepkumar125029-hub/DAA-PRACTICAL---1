import time

# Function for Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    # Bubble Sort Algorithm
    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop if already sorted
        if not swapped:
            break

# User Input
n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    value = int(input())
    arr.append(value)

print("\nOriginal List:", arr)

# Start Timer
start_time = time.perf_counter()

# Sorting
bubble_sort(arr)

# End Timer
end_time = time.perf_counter()

execution_time = end_time - start_time

print("\nSorted List:", arr)

print(f"\nExecution Time: {execution_time:.10f} seconds")

print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")

print("\nSpace Complexity:")
print("O(1)")