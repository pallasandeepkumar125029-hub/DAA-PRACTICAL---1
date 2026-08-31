# Practical 2: Linear Search and Binary Search

## Summary

Linear search and binary search are two common searching techniques used to find an element in a list. Both algorithms aim to check whether a target value exists in the given data, but they work differently and have different performance levels.

### Linear Search
Linear search checks each element one by one from the beginning of the list until the target is found or the list ends. It is simple to implement and does not require the data to be sorted. This makes it useful for small or unsorted datasets. However, in the worst case, it may need to scan the entire list, so its time complexity is O(n).

### Binary Search
Binary search is a more efficient technique that works only on sorted data. It repeatedly divides the search interval in half and compares the target with the middle element. If the target is smaller, it searches the left half; if larger, it searches the right half. This reduces the search space quickly, so the time complexity is O(log n), which is much faster than linear search for large datasets.

## Comparison

- Linear Search:
  - Works on sorted and unsorted arrays
  - Simple and easy to understand
  - Time complexity: O(1) best case, O(n) average and worst case
  - Space complexity: O(1)

- Binary Search:
  - Works only on sorted arrays
  - Faster for large datasets
  - Time complexity: O(1) best case, O(log n) average and worst case
  - Space complexity: O(1)

## Conclusion

Both linear and binary search are important algorithms in data structures and algorithms. Linear search is useful when the list is small or unsorted, because it is easy to implement and does not require sorting. Binary search is more efficient for large sorted datasets, as it reduces the search space by half each step. In conclusion, linear search is suitable for simple and small inputs, while binary search is preferred for faster searching in sorted data.

Therefore, the choice of algorithm depends on the nature of the data and the size of the problem. For sorted data, binary search is the better option; for unsorted or small data, linear search is often enough.
