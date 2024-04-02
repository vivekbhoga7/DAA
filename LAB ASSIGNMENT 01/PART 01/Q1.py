import time 
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10**6)

def iterative_algorithm(N):
    final_result = 0
    for i in range(1, N+1):
        final_result = final_result + i
    return final_result

def recursive_algorithm(N):
    if N == 0:
        return 0
    else:
        return N + recursive_algorithm(N-1)

def measure_time_iterative():
    times = []
    for n in [10, 100, 1000, 10000]:
        start_time = time.time()
        result = iterative_algorithm(n)
        end_time = time.time()
        times.append(end_time-start_time)
    return times

def measure_time_recursive():
    times = []
    for n in [10, 100, 1000, 10000]:
        start_time = time.time()
        result = recursive_algorithm(n)
        end_time = time.time()
        times.append(end_time-start_time)
    return times

iterative_time = measure_time_iterative()
recursive_time = measure_time_recursive()

N_values = [10, 100, 1000, 10000]
plt.plot(N_values, iterative_time, label='Iterative Algorithm')
plt.plot(N_values, recursive_time, label='Recursive Algorithm')
plt.xlabel('N')
plt.ylabel('Time (seconds)')
plt.title('Time taken to compute sum of N natural numbers')
plt.legend()
plt.show()