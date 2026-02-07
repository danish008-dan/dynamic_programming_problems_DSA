"""
Purpose:
--------
Solve the 0/1 Knapsack problem using Dynamic Programming.

Each item can either be included or excluded.
Goal is to maximize total value without exceeding capacity.
"""

def knapsack_01(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table row by row
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If current item weight is less than capacity
            if weights[i - 1] <= w:
                # Choose max of include or exclude
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                # Cannot include the item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

print("Maximum value:", knapsack_01(weights, values, capacity))
