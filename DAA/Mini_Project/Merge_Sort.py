import time
import random
import threading

# Single-threaded sort Implementation
# Merge function to merge two halves
def merge(arr, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    # Create temp arrays
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