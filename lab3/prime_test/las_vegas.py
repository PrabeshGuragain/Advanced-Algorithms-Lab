import random

def is_prime(n, k=5):
    """ Test if a number is prime using the Las Vegas algorithm with k trials """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Try k random trials
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
        if pow(a, n - 1, n) != 1:
            return False

    return True

def main():
    number = int(input("Enter a number to check for primality: "))
    trials = int(input("Enter the number of trials: "))
    if is_prime(number, trials):
        print(f"{number} is probably prime.")
    else:
        print(f"{number} is composite.")

if __name__ == "__main__":
    main()