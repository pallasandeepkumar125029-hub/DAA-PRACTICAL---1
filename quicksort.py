import time

def quick_sort(arr):
    # Base case: if the list is empty or has 1 element, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Picking the middle element as the pivot
        pivot = arr[len(arr) // 2]
        
        # Split the array into three parts
        left = [x for x in arr if x < pivot]      # Elements smaller than pivot
        middle = [x for x in arr if x == pivot]    # Elements equal to pivot
        right = [x for x in arr if x > pivot]     # Elements larger than pivot
        
        # Recursively sort the left and right parts, then combine them
        return quick_sort(left) + middle + quick_sort(right)

# --- User Input Section ---
if __name__ == "__main__":
    # Request numbers from the user separated by spaces
    user_input = input("Enter numbers separated by spaces (e.g., 5 2 9 1 7): ")
    
    # Convert the string input into a list of integers
    try:
        numbers = [int(x) for x in user_input.split()]
        
        print("\nOriginal List:", numbers)
        
        # Record the time right before starting the sort
        start_time = time.perf_counter()
        
        # Run the sorting algorithm
        sorted_list = quick_sort(numbers)
        
        # Record the time right after the sort finishes
        end_time = time.perf_counter()
        
        # Calculate execution time (End - Start)
        execution_time = end_time - start_time
        
        # Print Results
        print("Sorted List:  ", sorted_list)
        print(f"Execution Time: {execution_time:.6f} seconds")
        
        # --- Time Complexity Info ---
        print("\n--- Time Complexity Analysis ---")
        print("Best Case: O(n log n)")
        print("Average Case: O(n log n)")
        print("Worst Case: O(n²) (Happens if the pivot choices are very poor)")
        
    except ValueError:
        print("Please enter valid integers separated by spaces.")
