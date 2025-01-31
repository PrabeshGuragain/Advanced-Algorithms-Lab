def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
if __name__ == "__main__":
    n = 10  # Change this value to generate more or fewer Fibonacci numbers
    for i in range(n):
        print(fibonacci(i))