import random 
import time
import math
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    # Sort the array
    arr.sort()
    
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

def measure_search_time(search_func, arr, target):
    start_time = time.time()
    search_func(arr, target)
    end_time = time.time()
    return end_time - start_time

N_values = [100, 500, 1000, 5000, 10000]
linear_times = []
binary_times = []

for N in N_values:
    arr = [random.randrange(1, 1000) for _ in range(N)]
    target = random.randrange(1, 1000)
    
    linear_time = measure_search_time(linear_search, arr, target)
    binary_time = measure_search_time(binary_search, arr, target)
    
    linear_times.append(linear_time)
    binary_times.append(binary_time)

# Plotting
plt.plot(N_values, linear_times, label='Linear Search')
plt.plot(N_values, binary_times, label='Binary Search')
plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds)')
plt.title('Time taken for Linear and Binary Search')
plt.legend()
plt.show()
