"""
Purpose:
--------
Given n stairs, you can climb either 1 or 2 steps.
This program calculates the number of distinct ways
to reach the top using Dynamic Programming.
"""

def climb_stairs(n):
    # If there are 0 or 1 stairs, only one way
    if n <= 1:
        return 1

    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 1
    dp[1] = 1

    # Fill DP table
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print("Ways to climb stairs:", climb_stairs(5))
