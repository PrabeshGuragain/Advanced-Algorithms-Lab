import multiprocessing

def worker(start, end, input_arr, output_arr):
    for i in range(start, end):
        output_arr[i] = output_arr[i - 1] + input_arr[i]

def prefix_sum(arr):
    n = len(arr)
    if n == 0:
        return []

    num_processes = multiprocessing.cpu_count()
    chunk_size = (n + num_processes - 1) // num_processes

    manager = multiprocessing.Manager()
    output_arr = manager.list([0] * n)
    processes = []

    for i in range(num_processes):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, n)
        p = multiprocessing.Process(target=worker, args=(start, end, arr, output_arr))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    for i in range(1, num_processes):
        start = i * chunk_size
        if start < n:
            offset = output_arr[start - 1]
            for j in range(start, min((i + 1) * chunk_size, n)):
                output_arr[j] += offset

    return list(output_arr)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    result = prefix_sum(arr)
    print("Original array:", arr)
    print("Prefix sum result:", result)
    total_sum = result[-1] if result else 0
    print("Total sum:", total_sum)