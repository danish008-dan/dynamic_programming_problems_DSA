"""
Purpose:
--------
Find the length of the Longest Increasing Subsequence (LIS)
in a given array using Dynamic Programming.
"""

def lis(nums):
    n = len(nums)

    # If array is empty
    if n == 0:
        return 0

    # DP array where dp[i] is LIS ending at index i
    dp = [1] * n

    # Compute LIS for each index
    for i in range(n):
        for j in range(i):
            # Extend increasing subsequence
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


print("LIS length:", lis([10, 9, 2, 5, 3, 7, 101, 18]))
