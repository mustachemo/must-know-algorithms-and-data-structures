# Fibonacci sequence using dynamic programming
def fibonacci(n):
    # Create an array to store Fibonacci numbers
    fib = [0] * (n + 1)

    # Base cases
    fib[0] = 0
    fib[1] = 1

    # Compute Fibonacci numbers iteratively
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


if __name__ == "__main__":
    n = 10
    result = fibonacci(n)
    print(f"The {n}-th Fibonacci number is {result}")
