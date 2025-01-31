import time
from fibonacci_dynamic import fibonacci as fibonacci_dynamic
from fibonacci_recurssion import fibonacci as fibonacci_recursion

import matplotlib.pyplot as plt

def measure_time(fib_func, n):
    start_time = time.time()
    fib_func(n)
    end_time = time.time()
    return end_time - start_time

def main():
    n_values = range(1, 31) 
    dynamic_times = []
    recursion_times = []

    for n in n_values:
        dynamic_times.append(measure_time(fibonacci_dynamic, n))
        recursion_times.append(measure_time(fibonacci_recursion, n))

    plt.plot(n_values, dynamic_times, label='Dynamic Programming')
    plt.plot(n_values, recursion_times, label='Recursion')
    plt.xlabel('N (Number of Terms)')
    plt.ylabel('Time (seconds)')
    plt.title('Fibonacci Series Generation Time Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()