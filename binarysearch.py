import time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is at mid
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # Target not found

# --- User Input Section ---
if __name__ == "__main__":
    # Request numbers from the user separated by spaces
    user_input = input("Enter numbers separated by spaces (e.g., 5 2 9 1 7): ")
    
    try:
        # Convert the string input into a list of integers
