import time

def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop for the rounds
    for i in range(n):
        swapped = False
        
        # Inner loop to compare adjacent numbers
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no numbers were swapped, the list is already sorted!
        if not swapped:
            break
            
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
        sorted_list = bubble_sort(numbers)
        
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
        print("Worst Case (Reverse Sorted): O(n²)")
        print("Average Case: O(n²)")
        
    except ValueError:
        print("Please enter valid integers separated by spaces.")
