Dynamic Programming – Core Problems
===================================

This repository contains fundamental Dynamic Programming problems
implemented in Python with clean code and clear explanations.
Each problem demonstrates how DP optimizes recursive solutions.

------------------------------------------------------------

1. Recursion vs Dynamic Programming
-----------------------------------

Problem Description:
Recursion solves problems by breaking them into smaller subproblems,
but it often recomputes the same values multiple times.

Dynamic Programming improves this by storing results of subproblems
and reusing them.

Concepts Demonstrated:
- Overlapping subproblems
- Time complexity reduction
- Memoization vs Tabulation

Key Learning:
Recursion can be inefficient for large inputs, while DP avoids
redundant calculations and improves performance.

------------------------------------------------------------

2. Fibonacci Sequence
---------------------

Problem Description:
Find the nth Fibonacci number where:
F(n) = F(n-1) + F(n-2)

DP Approach:
Instead of recalculating values recursively, previous results
are stored and reused.

Techniques Used:
- Bottom-up Dynamic Programming
- Space optimization

Time Complexity:
O(n)

Space Complexity:
O(1)

------------------------------------------------------------

3. Climbing Stairs
-----------------

Problem Description:
Given n stairs, you can climb either 1 or 2 steps at a time.
Find the number of distinct ways to reach the top.

DP Insight:
The number of ways to reach step n depends on:
ways(n-1) + ways(n-2)

This problem is similar to the Fibonacci pattern.

Time Complexity:
O(n)

Space Complexity:
O(n)

Applications:
- Path counting problems
- Combinatorics
- Interview problem patterns

------------------------------------------------------------

4. 0/1 Knapsack Problem
----------------------

Problem Description:
Given items with weights and values, and a knapsack capacity,
determine the maximum value that can be obtained.
Each item can be either taken or not taken.

DP Approach:
A 2D DP table is used where:
dp[i][w] represents the maximum value using first i items
with capacity w.

Concepts Demonstrated:
- Optimal substructure
- Decision making (include or exclude)
- Two-dimensional DP

Time Complexity:
O(n * capacity)

Space Complexity:
O(n * capacity)

Applications:
- Resource allocation
- Budget optimization
- Logistics and planning systems

------------------------------------------------------------

Core Dynamic Programming Concepts
---------------------------------
- Overlapping Subproblems
- Optimal Substructure
- Memoization (Top-Down)
- Tabulation (Bottom-Up)
- Space Optimization

------------------------------------------------------------

Why Learn Dynamic Programming
-----------------------------
- Essential for coding interviews
- Helps solve optimization problems
- Improves performance of recursive solutions
- Widely used in competitive programming

------------------------------------------------------------

Unbounded Knapsack Problem
==========================

Problem Description
-------------------
Given a set of items, each with a weight and a value,
and a knapsack with a fixed capacity, determine the
maximum value that can be obtained.

Unlike the 0/1 Knapsack problem, each item can be taken
an unlimited number of times.

Dynamic Programming Approach
----------------------------
A one-dimensional DP array is used where:
dp[w] represents the maximum value achievable
with knapsack capacity w.

For each capacity, all items are considered and
the best possible value is stored.

Key Concepts
------------
- Overlapping subproblems
- Optimal substructure
- Unbounded choice of items
- Space optimized DP

Time Complexity
---------------
O(n * capacity)

Space Complexity
----------------
O(capacity)

Applications
------------
- Rod cutting problem
- Resource allocation with repetition
- Manufacturing and packing optimization

Longest Common Subsequence and Longest Increasing Subsequence
=============================================================

Overview
--------
This module covers two important Dynamic Programming problems
that focus on sequence comparison and optimization.

------------------------------------------------------------

1. Longest Common Subsequence (LCS)
----------------------------------

Problem Description:
Given two sequences, find the length of the longest subsequence
that appears in both sequences in the same order.

Dynamic Programming Approach:
A 2D DP table is used where dp[i][j] represents the length
of the LCS of the first i characters of string one and
first j characters of string two.

Time Complexity:
O(n * m)

Space Complexity:
O(n * m)

Applications:
- DNA sequence analysis
- File comparison tools
- Version control systems

------------------------------------------------------------

2. Longest Increasing Subsequence (LIS)
--------------------------------------

Problem Description:
Given an array of integers, find the length of the longest
subsequence such that elements are in strictly increasing order.

Dynamic Programming Approach:
For each index, compute the LIS ending at that index by
checking all previous elements.

Time Complexity:
O(n^2)

Space Complexity:
O(n)

Applications:
- Stock analysis
- Sequence optimization
- Pattern recognition

------------------------------------------------------------

Key DP Concepts Used
-------------------
- Tabulation (Bottom-Up DP)
- Optimal substructure
- Overlapping subproblems

Matrix Chain Multiplication and Coin Change
===========================================

Overview
--------
This module covers two important Dynamic Programming problems
focused on optimization and decision making.

------------------------------------------------------------

1. Matrix Chain Multiplication
------------------------------

Problem Description:
Given a sequence of matrices, determine the most efficient
way to multiply them by minimizing the total number of
scalar multiplications.

Dynamic Programming Approach:
A 2D DP table is used where dp[i][j] represents the minimum
cost to multiply matrices from index i to j.

The algorithm tries all possible split points to find
the optimal solution.

Time Complexity:
O(n^3)

Space Complexity:
O(n^2)

Applications:
- Compiler optimization
- Expression evaluation
- Scientific computing

------------------------------------------------------------

2. Coin Change Problem
---------------------

Problem Description:
Given a set of coin denominations and a target amount,
determine the minimum number of coins required to make
that amount.

Dynamic Programming Approach:
A one-dimensional DP array is used where dp[x] represents
the minimum coins needed to form amount x.

This is an example of unbounded knapsack variation.

Time Complexity:
O(n * amount)

Space Complexity:
O(amount)

Applications:
- Currency systems
- Payment optimization
- Resource allocation

------------------------------------------------------------

Key Concepts Used
----------------
- Tabulation
- Space Optimization
- Optimal substructure
- Overlapping subproblems

----------------------------------------------------------
Subset Sum and Palindrome Dynamic Programming
=============================================

Overview
--------
This module covers two classic Dynamic Programming problems
that focus on decision making and string optimization.

------------------------------------------------------------

1. Subset Sum Problem
--------------------

Problem Description:
Given a set of integers and a target sum, determine whether
there exists a subset whose elements add up exactly to
the target value.

Dynamic Programming Approach:
A 2D DP table is used where dp[i][s] indicates whether
a sum s can be achieved using the first i elements.

Time Complexity:
O(n * target)

Space Complexity:
O(n * target)

Applications:
- Partition problems
- Resource allocation
- Decision making systems

------------------------------------------------------------

2. Palindrome Dynamic Programming
--------------------------------

Problem Description:
Given a string, determine the length of the longest
palindromic subsequence present in the string.

Dynamic Programming Approach:
A 2D DP table is used where dp[i][j] represents the
length of the longest palindromic subsequence between
indices i and j.

Time Complexity:
O(n^2)

Space Complexity:
O(n^2)

Applications:
- Text processing
- DNA sequence analysis
- Pattern recognition

------------------------------------------------------------

Key Concepts Used
----------------
- Tabulation
- Optimal substructure
- Overlapping subproblems

------------------------------------------------------------

Author
------
Danish Khatri
