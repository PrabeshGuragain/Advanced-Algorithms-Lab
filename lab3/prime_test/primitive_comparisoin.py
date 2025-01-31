import random
import time

import matplotlib.pyplot as plt

# Monte Carlo: Miller-Rabin Primality Test
def is_probably_prime_monte_carlo(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    def miller_rabin_test(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if not miller_rabin_test(a):
            return False

    return True  # Probably prime

# Las Vegas: Randomized Trial Division
def is_prime_las_vegas(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    for _ in range(int(n**0.5)):
        divisor = random.randint(2, int(n**0.5))
        if n % divisor == 0:
            return False  # Found a divisor
    return True  # If no divisor is found

# Measure time complexity
def measure_time_complexity(test_function, inputs):
    times = []
    for n in inputs:
        start_time = time.time()
        test_function(n)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

# Test range of numbers
input_sizes = [10**x for x in range(1, 6)]  # Numbers like 10, 100, 1000, 10000, 100000
monte_carlo_times = measure_time_complexity(lambda n: is_probably_prime_monte_carlo(n, k=5), input_sizes)
las_vegas_times = measure_time_complexity(is_prime_las_vegas, input_sizes)

# Plot the time complexity
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, monte_carlo_times, label="Monte Carlo (Miller-Rabin)", marker="o")
plt.plot(input_sizes, las_vegas_times, label="Las Vegas (Trial Division)", marker="o")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (s)")
plt.title("Time Complexity: Monte Carlo vs. Las Vegas Primality Test")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()