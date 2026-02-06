"""
Purpose:
--------
Find the nth Fibonacci number using
Dynamic Programming with optimized space.
"""

def fibonacci(n):
    # Handle base cases
    if n <= 1:
        return n

    prev2 = 0  # F(0)
    prev1 = 1  # F(1)

    # Compute Fibonacci iteratively
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


print("Fibonacci number:", fibonacci(10))
