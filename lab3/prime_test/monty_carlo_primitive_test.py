import random

def miller_rabin_test(n, k):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Write n as d*2^r + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Example usage
if __name__ == "__main__":
    n = 561  # Example number to test
    k = 5    # Number of iterations
    if miller_rabin_test(n, k):
        print(f"{n} is probably prime.")
    else:
        print(f"{n} is composite.")