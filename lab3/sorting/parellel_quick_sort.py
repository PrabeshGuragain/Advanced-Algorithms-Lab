import multiprocessing
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def parallel_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    with multiprocessing.Pool(processes=4) as pool:
        left, right = pool.map(quicksort, [left, right])

    return left + middle + right

if __name__ == "__main__":
    arr = [random.randint(0, 100) for _ in range(100)]
    print("Original array:", arr)
    sorted_arr = parallel_quicksort(arr)
    print("Sorted array:", sorted_arr)