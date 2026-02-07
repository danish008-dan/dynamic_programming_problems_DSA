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
