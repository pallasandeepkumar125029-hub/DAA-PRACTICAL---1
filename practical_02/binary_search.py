import time

# Binary Search Function
# Works only for sorted list.
# This uses a loop and manual midpoint calculation
# without any built-in search function.
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# User Input
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements in sorted order:")
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter the element to search: "))

print("\nOriginal List:", arr)

# Start Timer
start_time = time.perf_counter()

# Search Operation
position = binary_search(arr, target)

# End Timer
end_time = time.perf_counter()
execution_time = end_time - start_time

if position != -1:
    print("\nElement found at position:", position + 1)
else:
    print("\nElement not found in the list")

print(f"\nExecution Time: {execution_time:.10f} seconds")

print("\nTime Complexity:")
print("Best Case    : O(1)")
print("Average Case : O(log n)")
print("Worst Case   : O(log n)")

print("\nSpace Complexity:")
print("O(1)")
