# Unique Paths

## Problem
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

![Robot_Maze](../images/robot_maze.png)

Note: m and n will be at most 100.

### Example 1:

    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right

## Solution

Solution I: Dynamic programming
A 2D table is set up with the same shape of the maze. Each element indicts the number of paths reaching the finish position.

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1] * n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[m-1][n-1]
```
