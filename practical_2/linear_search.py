import time

# Linear Search Function
# This function checks each element one by one
# without using any built-in search function.
def linear_search(arr, target):
    n = len(arr)

    for i in range(n):
        if arr[i] == target:
            return i

    return -1

# User Input
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter the element to search: "))

print("\nOriginal List:", arr)

# Start Timer
start_time = time.perf_counter()

# Search Operation
position = linear_search(arr, target)

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
print("Average Case : O(n)")
print("Worst Case   : O(n)")

print("\nSpace Complexity:")
print("O(1)")
