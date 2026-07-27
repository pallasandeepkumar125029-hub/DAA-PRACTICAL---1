import time

def insertion_sort(arr):
    # Start from the second element (index 1) as the first element is "sorted"
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Insert the key into its correct sorted position
        arr[j + 1] = key
        
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
        sorted_list = insertion_sort(numbers)
        
        # Record the time right after the sort finishes
        end_time = time.perf_counter()
        
        # Calculate execution time (End - Start)
        execution_time = end_time - start_time
        
        # Print Results
        print("Sorted List:  ", sorted_list)
        print(f"Execution Time: {execution_time:.6f} seconds")
        
        # --- Time Complexity Info ---
        print("\n--- Time Complexity Analysis ---")
        print("Best Case (Already Sorted): O(n)")
        print("Average Case: O(n²)")
        print("Worst Case (Reverse Sorted): O(n²)")
        print("\nNote: Like Bubble Sort, Insertion Sort has an excellent best-case scenario.")
        print("If the list is already sorted, the inner loop never shifts numbers,")
        print("making it highly efficient for nearly-sorted data.")
        
    except ValueError:
        print("Please enter valid integers separated by spaces.")
        