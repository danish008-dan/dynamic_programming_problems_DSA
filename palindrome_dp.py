"""
Purpose:
--------
Find the length of the Longest Palindromic Subsequence
in a given string using Dynamic Programming.
"""

def longest_palindromic_subsequence(s):
    n = len(s)

    # Create DP table
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build DP table for substrings of increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # If characters match
            if s[i] == s[j]:
                dp[i][j] = 2 if length == 2 else 2 + dp[i + 1][j - 1]
            else:
                # Take maximum by excluding one character
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


print("Longest Palindromic Subsequence length:",
      longest_palindromic_subsequence("bbbab"))
