"""
Purpose:
--------
Determine whether there exists a subset of a given set
with sum equal to a given target value using
Dynamic Programming.
"""

def subset_sum(nums, target):
    n = len(nums)

    # Create DP table where dp[i][s] means:
    # using first i elements, can we make sum s
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    # Base case: sum 0 is always possible (empty subset)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill DP table
    for i in range(1, n + 1):
        for s in range(1, target + 1):
            # Exclude current element
            dp[i][s] = dp[i - 1][s]

            # Include current element if possible
            if nums[i - 1] <= s:
                dp[i][s] = dp[i][s] or dp[i - 1][s - nums[i - 1]]

    return dp[n][target]


nums = [3, 34, 4, 12, 5, 2]
target = 9

print("Subset with given sum exists:", subset_sum(nums, target))
