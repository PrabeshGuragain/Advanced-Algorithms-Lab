import time
from NqueensBruteforce import solve_nqueens as solve_nqueens_bruteforce
from NQueensBacktracking import solve_nqueens as solve_nqueens_backtracking

import matplotlib.pyplot as plt

def measure_time(n, solve_nqueens):
    start_time = time.time()
    solve_nqueens(n)
    end_time = time.time()
    return end_time - start_time

def main():
    n_values = range(4, 12)  # Adjust the range as needed
    bruteforce_times = []
    backtracking_times = []

    for n in n_values:
        bruteforce_times.append(measure_time(n, solve_nqueens_bruteforce))
        backtracking_times.append(measure_time(n, solve_nqueens_backtracking))

    plt.plot(n_values, bruteforce_times, label='Bruteforce Algorithm')
    plt.plot(n_values, backtracking_times, label='Backtracking Algorithm')
    plt.xlabel('N (Number of Queens)')
    plt.ylabel('Time (seconds)')
    plt.title('N-Queens Algorithm Time Complexity Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()