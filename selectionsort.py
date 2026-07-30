import time

def selection_sort(arr):
    n = len(arr)
    
    # Move the boundary of the unsorted subarray
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    return arr

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
        sorted_list = selection_sort(numbers)
        
        # Record the time right after the sort finishes
        end_time = time.perf_counter()
        
        # Calculate execution time (End - Start)
        execution_time = end_time - start_time
        
        # Print Results
        print("Sorted List:  ", sorted_list)
        print(f"Execution Time: {execution_time:.6f} seconds")
        
        # --- Time Complexity Info ---
        print("\n--- Time Complexity Analysis ---")
        print("Best Case: O(n²)")
        print("Average Case: O(n²)")
        print("Worst Case: O(n²)")
        print("\nNote: Unlike Bubble Sort, Selection Sort always takes O(n²) time")
        print("because it must scan the remaining unsorted list to find the minimum,")
        print("even if the list is already completely sorted.")
        
    except ValueError:
        print("Please enter valid integers separated by spaces.")
