
## Intro
This repository contains implementations of common sorting algorithms used in the study of data structures and algorithms. Each file demonstrates a different sorting technique with clear, standalone Python code.

## Bubble Sort

### Introduction
`bubble_sort.py` implements the bubble sort algorithm, which repeatedly steps through the list and swaps adjacent elements until the list is sorted.

### Summary
This algorithm is simple and easy to understand, but it is less efficient on large datasets due to its quadratic time complexity.

### Conclusion
Use bubble sort for learning and small inputs. It is not ideal for performance-sensitive scenarios.

##-------------------------------------------------------------------------------------------

## Insertion Sort

### Introduction
`insertion_sort.py` implements insertion sort, which builds a sorted portion of the list by inserting one element at a time.

### Summary
Insertion sort is efficient for nearly sorted data and small arrays, with average-case quadratic time complexity.

### Conclusion
This algorithm is useful for small or partially sorted datasets and as a learning tool for algorithm behavior.

##-------------------------------------------------------------------------------------------

## Selection Sort

### Introduction
`selection_sort.py` implements selection sort, which repeatedly selects the smallest remaining element and moves it to the sorted portion.

### Summary
Selection sort is straightforward and has predictable performance, but it is not efficient for large lists.

### Conclusion
Use selection sort for educational purposes and when algorithm simplicity is more important than speed.

##-------------------------------------------------------------------------------------------

## Merge Sort
### Introduction
`merge_sort.py` implements merge sort, a divide-and-conquer algorithm that splits the list, sorts the halves, and merges them.

### Summary
Merge sort has good performance with O(n log n) time complexity and is stable, making it suitable for larger datasets.

### Conclusion
Choose merge sort for larger data or when stable sorting is required.

##-------------------------------------------------------------------------------------------

## Quick Sort

### Introduction
`quick_sort.py` implements quick sort, which partitions the list around a pivot and recursively sorts the partitions.

### Summary
Quick sort is often fast in practice with average O(n log n) time, but worst-case quadratic behavior can occur without careful pivot selection.

### Conclusion
Quick sort is a strong general-purpose sort for many datasets when implemented with good pivot strategy.

##-------------------------------------------------------------------------------------------

## Overall Conclusion
This lab provides a concise reference for five fundamental sorting methods. Each implementation is useful for understanding algorithm trade-offs and comparing performance characteristics.
