import time

def merge_sort(arr):
    # Base case: if the list has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle point to divide the array
    mid = len(arr) // 2
    
    # Recursively sort the left and right halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0
    
    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Add remaining elements (if any)
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# --- User Input Section ---
if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces (e.g., 5 2 9 1 7): ")
    
    try:
        numbers = [int(x
