# filepath: /E:/Lab/Algo/lab3/sorting/parellel_sort_compare.py
import sys
import os
import time
import random

lab1_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Lab1'))
sys.path.insert(0, lab1_path)

from heap_sort import heap_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort as normal_merge_sort
from quick_sort import quick_sort as normal_quick_sort
from selection_sort import selection_sort
from parellel_quick_sort import parallel_quicksort
from parellel_merge_sort import parallel_merge_sort


import matplotlib.pyplot as plt

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

def main():
    input_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
    algorithms = {
        "Heap Sort": heap_sort,
        # "Insertion Sort": insertion_sort,
        # "Bubble Sort": bubble_sort,
        "Merge Sort": normal_merge_sort,
        "Quick Sort": normal_quick_sort,
        # "Selection Sort": selection_sort,
        "Parallel Quick Sort": parallel_quicksort,
        # "Parallel Merge Sort": parallel_merge_sort
    }
    
    results = {name: [] for name in algorithms.keys()}
    
    for size in input_sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        for name, func in algorithms.items():
            arr_copy = arr.copy()
            time_taken = measure_time(func, arr_copy)
            results[name].append(time_taken)
    
    for name, times in results.items():
        plt.plot(input_sizes, times, label=name)
    
    plt.xlabel('Input Size')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Comparison of Sorting Algorithms with 4 Processes')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()