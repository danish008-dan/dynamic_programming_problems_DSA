"""
Purpose:
--------
Solve the Unbounded Knapsack problem using
Dynamic Programming.

Each item can be taken unlimited number of times.
The goal is to maximize total value within given capacity.
"""

def unbounded_knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP array where dp[w] stores maximum value for capacity w
    dp = [0] * (capacity + 1)

    # Fill DP table
    for w in range(capacity + 1):
        for i in range(n):
            # Check if item can fit in current capacity
            if weights[i] <= w:
                # Take maximum of including or excluding the item
                dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]


weights = [2, 3, 4]
values = [5, 7, 8]
capacity = 10

print("Maximum value:", unbounded_knapsack(weights, values, capacity))
