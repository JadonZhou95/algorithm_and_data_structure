# Climbing Stairs

## Problem
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

### Example 1:

    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

## Solution

### I. Dynamic Programming
Actually, it works like a Fibonachi Arrays
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(n - 2):
            a, b = b, a + b
            
        return b
```
Complexity
* Time: O(n)
* Memory: O(1)