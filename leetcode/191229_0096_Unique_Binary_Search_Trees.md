# Unique Binary Search Trees

## Problem
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

    Input: 3
    Output: 5
    Explanation:
    Given n = 3, there are a total of 5 unique BST's:

        1         3     3      2      1
         \       /     /      / \      \
          3     2     1      1   3      2
         /     /       \                 \
        2     1         2                 3

## Solution
### I. Dynamic Programming
```python
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        
        coeffs = [1]
        for i in range(n - 2):
            sum_value = 0
            for i in range(len(coeffs)):
                sum_value += coeffs[i]
                coeffs[i] = sum_value
            coeffs.append(coeffs[-1])
        
        result = 0
        for coeff in coeffs:
            result += n * coeff
            n -= 1
        
        return result
```

Complexity
* Time: O(n^2)
* Memory: O(n)

