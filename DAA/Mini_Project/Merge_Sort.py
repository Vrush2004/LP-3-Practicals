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