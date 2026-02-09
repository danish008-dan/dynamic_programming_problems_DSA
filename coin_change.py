"""
Purpose:
--------
Solve the Coin Change problem using Dynamic Programming.

Given coin denominations and a target amount,
find the minimum number of coins needed to make the amount.
"""

def coin_change(coins, amount):
    # Initialize DP array with a large value
    dp = [float('inf')] * (amount + 1)

    # Base case
    dp[0] = 0

    # Build DP table
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] = min(dp[a], dp[a - coin] + 1)

    # If amount cannot be formed, return -1
    return dp[amount] if dp[amount] != float('inf') else -1


coins = [1, 2, 5]
amount = 11

print("Minimum coins required:", coin_change(coins, amount))
