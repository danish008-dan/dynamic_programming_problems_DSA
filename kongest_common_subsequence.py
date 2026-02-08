"""
Purpose:
--------
Find the length of the Longest Common Subsequence (LCS)
between two strings using Dynamic Programming.
"""

def lcs(text1, text2):
    n = len(text1)
    m = len(text2)

    # Create DP table
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If characters match, extend the subsequence
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # Take maximum of excluding one character
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


print("LCS length:", lcs("abcde", "ace"))
