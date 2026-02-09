"""
Purpose:
--------
Solve the Matrix Chain Multiplication problem using
Dynamic Programming.

The goal is to find the minimum number of scalar
multiplications needed to multiply a chain of matrices.
"""

def matrix_chain_order(dims):
    n = len(dims) - 1

    # Create DP table
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # l is chain length
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')

            # Try all possible splits
            for k in range(i, j):
                cost = (
                    dp[i][k] +
                    dp[k + 1][j] +
                    dims[i] * dims[k + 1] * dims[j + 1]
                )
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


dimensions = [1, 2, 3, 4]
print("Minimum multiplications:", matrix_chain_order(dimensions))
