def fibonacci(n):
    # Base conditions: Fibonacci of 0 is 0 and Fibonacci of 1 is 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive return: Fibonacci of n = Fibonacci of (n-1) + Fibonacci of (n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
number = 6
result = fibonacci(number)
print("Fibonacci of", number, "is", result)


