# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:49:55 2024

@author: hp
"""

import random
import time
import csv

# Insertion Sort algorithm
def insertion_sort(arr):
    """Sorts an array using the insertion sort algorithm."""
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp  

# Merge Sort algorithm
def merge_sort(arr):
    """Sorts an array using the merge sort algorithm."""
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0  # Initial indexes for left, right, and merged arrays

        # Merging the two halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copying the remaining elements of L[], if any
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copying the remaining elements of R[], if any
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def hybrid_merge_sort(arr):
    """Sorts an array using hybrid merge sort with insertion sort for small arrays."""
    if len(arr) <= 50:  # Threshold for switching to insertion sort
        insertion_sort(arr)
    else:  # Using merge sort for larger arrays
        merge_sort(arr)

# Bubble Sort algorithm
def bubble_sort(arr):
    """Sorts an array using the bubble sort algorithm."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Break if no elements were swapped
            break

# Selection Sort algorithm
def selection_sort(arr):
    """Sorts an array using the selection sort algorithm."""
    n = len(arr)
    for i in range(n):
        mini_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini_index]:
                mini_index = j
        arr[i], arr[mini_index] = arr[mini_index], arr[i]

def measure_time(sort_function, arr):
    """Measures the runtime of a sorting function."""
    start_time = time.time()
    sort_function(arr.copy())  # Copy the array to avoid in-place sorting affecting other tests
    end_time = time.time()
    return end_time - start_time

# Generate a random array of length n
def generate_random_array(n):
    """Generates a random array of length n with values between 0 and n."""
    return [random.randint(0, n) for _ in range(n)]

def read_n_values(filename):
    """Reads integer values from a file, one per line."""
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]

# Read the array sizes from 'Nvalues.txt'
n_values = read_n_values('Nvalues.txt')

results = []

# Process each array size
for n in n_values:
    print(f"Processing n = {n}")
    arr = generate_random_array(n)
    
    # Measure the runtime for each sorting algorithm
    insertion_time = measure_time(insertion_sort, arr)
    merge_time = measure_time(merge_sort, arr)
    hybrid_merge_time = measure_time(hybrid_merge_sort, arr)
    selection_time = measure_time(selection_sort, arr)
    bubble_time = measure_time(bubble_sort, arr)
    
    # Store the results
    results.append([n, insertion_time, merge_time, hybrid_merge_time, selection_time, bubble_time])

# Save the results to 'RunTime.csv'
with open('RunTime.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Value of n', 'Insertion Sort (seconds)', 'Merge Sort (seconds)', 'Hybrid Merge Sort (seconds)', 'Selection Sort (seconds)', 'Bubble Sort (seconds)'])
    writer.writerows(results)

print("Results saved to RunTime.csv.")
