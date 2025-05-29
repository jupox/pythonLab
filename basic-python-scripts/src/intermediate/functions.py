def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers. Raises an error if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def factorial(n):
    """Returns the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a