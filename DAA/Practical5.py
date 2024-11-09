import time
import random
import threading

# Single-threaded sort Implementation
# Merge function to merge two halves
def merge(arr, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle
    L = arr[left:left + n1]
    R = arr[middle + 1:middle + 1 + n2]

    i = j = 0  # Initial indexes of subarrays
    k = left  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Merge sort function
def merge_sort(arr, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)
        merge(arr, left, middle, right)

# Timing single-threaded merge sort
def time_merge_sort(arr):
    start_time = time.time()
    merge_sort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

# Multithreaded merge sort function
def merge_sort_multithreaded(arr, left, right):
    if left < right:
        middle = (left + right) // 2
        
        # Create threads for both halves
        left_thread = threading.Thread(target=merge_sort_multithreaded, args=(arr, left, middle))
        right_thread = threading.Thread(target=merge_sort_multithreaded, args=(arr, middle + 1, right))
        
        left_thread.start()
        right_thread.start()

        left_thread.join()
        right_thread.join()
        
        merge(arr, left, middle, right)

# Timing multithreaded merge sort
def time_multithreaded_merge_sort(arr):
    start_time = time.time()
    merge_sort_multithreaded(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

# Performance Comparison and Analysis
# Generate best-case and worst-case arrays
best_case = list(range(10000))  # Already sorted array (best case)
worst_case = list(range(10000, 0, -1))  # Reverse sorted array (worst case)

# Make copies of the arrays for each test
best_case_single = best_case.copy()
best_case_multi = best_case.copy()
worst_case_single = worst_case.copy()
worst_case_multi = worst_case.copy()

# Time single-threaded and multithreaded merge sort for best case
print("Best Case Performance:")
single_threaded_time_best = time_merge_sort(best_case_single)
print(f"Single-threaded Merge Sort: {single_threaded_time_best:.4f} seconds")

multi_threaded_time_best = time_multithreaded_merge_sort(best_case_multi)
print(f"Multithreaded Merge Sort: {multi_threaded_time_best:.4f} seconds")

# Time single-threaded and multithreaded merge sort for worst case
print("\nWorst Case Performance:")
single_threaded_time_worst = time_merge_sort(worst_case_single)
print(f"Single-threaded Merge Sort: {single_threaded_time_worst:.4f} seconds")

multi_threaded_time_worst = time_multithreaded_merge_sort(worst_case_multi)
print(f"Multithreaded Merge Sort: {multi_threaded_time_worst:.4f} seconds")


# import time
# import random
# import threading
# time is used to measure the performance of the algorithms.
# random would be useful if you wanted to create randomly shuffled arrays (though it's not used in this code).
# threading allows for multi-threading, which we use to parallelize the sorting process in the multi-threaded merge sort.
# Merge Sort: Single-Threaded Implementation
# Merge Function
# python
# Copy code
# def merge(arr, left, middle, right):
# Merges two sorted halves of an array, arr, between the indices left and right.
# middle represents the end of the left sub-array and start of the right sub-array.
# python
# Copy code
#     n1 = middle - left + 1
#     n2 = right - middle
# n1 and n2 represent the lengths of the left (L) and right (R) sub-arrays.
# python
# Copy code
#     L = arr[left:left + n1]
#     R = arr[middle + 1:middle + 1 + n2]
# Copies elements from arr to form L (left sub-array) and R (right sub-array).
# python
# Copy code
#     i = j = 0  # Initial indexes of subarrays
#     k = left  # Initial index of merged subarray
# i and j are pointers for L and R respectively, while k is the index for the main arr.
# python
# Copy code
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
# Compares elements of L and R, placing the smaller element into arr at position k.
# Increments i, j, or k as appropriate to move through the sub-arrays.
# python
# Copy code
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
# Adds any remaining elements from L or R to arr (if one half is fully merged before the other).
# Recursive Merge Sort Function
# python
# Copy code
# def merge_sort(arr, left, right):
#     if left < right:
#         middle = (left + right) // 2
# The function recursively divides arr into two halves until left and right pointers indicate a sub-array of one element, which is inherently sorted.
# python
# Copy code
#         merge_sort(arr, left, middle)
#         merge_sort(arr, middle + 1, right)
#         merge(arr, left, middle, right)
# Recursively sorts the left and right halves and then merges them using merge.
# Timing the Single-Threaded Merge Sort
# python
# Copy code
# def time_merge_sort(arr):
#     start_time = time.time()
#     merge_sort(arr, 0, len(arr) - 1)
#     end_time = time.time()
#     return end_time - start_time
# Records the start and end times of the single-threaded merge_sort, returning the time taken to sort arr.
# Multi-Threaded Merge Sort
# Recursive Multi-Threaded Merge Sort Function
# python
# Copy code
# def merge_sort_multithreaded(arr, left, right):
#     if left < right:
#         middle = (left + right) // 2
# Similar to merge_sort, merge_sort_multithreaded recursively divides arr.
# python
# Copy code
#         left_thread = threading.Thread(target=merge_sort_multithreaded, args=(arr, left, middle))
#         right_thread = threading.Thread(target=merge_sort_multithreaded, args=(arr, middle + 1, right))
# Creates two threads (left_thread and right_thread) to handle the sorting of the left and right halves of the array simultaneously.
# python
# Copy code
#         left_thread.start()
#         right_thread.start()
#         left_thread.join()
#         right_thread.join()
# Starts both threads, and join ensures the program waits until both threads finish before proceeding to the merge step.
# python
# Copy code
#         merge(arr, left, middle, right)
# Once both threads complete, merge is called to combine the sorted halves.
# Timing the Multi-Threaded Merge Sort
# python
# Copy code
# def time_multithreaded_merge_sort(arr):
#     start_time = time.time()
#     merge_sort_multithreaded(arr, 0, len(arr) - 1)
#     end_time = time.time()
#     return end_time - start_time
# Records the time taken to sort arr using the multi-threaded merge sort.
# Performance Comparison and Analysis
# python
# Copy code
# best_case = list(range(10000))  # Already sorted array (best case)
# worst_case = list(range(10000, 0, -1))  # Reverse sorted array (worst case)
# best_case is an already sorted array, ideal for merge sort’s performance.
# worst_case is reverse sorted, representing a challenging input for many sorting algorithms.
# python
# Copy code
# best_case_single = best_case.copy()
# best_case_multi = best_case.copy()
# worst_case_single = worst_case.copy()
# worst_case_multi = worst_case.copy()
# Creates copies of best_case and worst_case to avoid altering the original arrays during testing.
# Timing Best-Case Sorting
# python
# Copy code
# print("Best Case Performance:")
# single_threaded_time_best = time_merge_sort(best_case_single)
# print(f"Single-threaded Merge Sort: {single_threaded_time_best:.4f} seconds")
# multi_threaded_time_best = time_multithreaded_merge_sort(best_case_multi)
# print(f"Multithreaded Merge Sort: {multi_threaded_time_best:.4f} seconds")
# Measures the time for both single-threaded and multi-threaded merge sort on the sorted array best_case.
# Outputs the times, showing whether multi-threading provides a performance boost in the best-case scenario.
# Timing Worst-Case Sorting
# python
# Copy code
# print("\nWorst Case Performance:")
# single_threaded_time_worst = time_merge_sort(worst_case_single)
# print(f"Single-threaded Merge Sort: {single_threaded_time_worst:.4f} seconds")
# multi_threaded_time_worst = time_multithreaded_merge_sort(worst_case_multi)
# print(f"Multithreaded Merge Sort: {multi_threaded_time_worst:.4f} seconds")
# Similarly, measures the time taken for sorting the reverse-sorted array worst_case with both versions of merge sort.
# Outputs the times, helping you see if multi-threading provides a significant speedup in the worst-case scenario.