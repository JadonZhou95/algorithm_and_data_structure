# Rotate Image

## Problem
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

### Example 2:

    Given input matrix =
    [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ], 

    rotate the input matrix in-place such that it becomes:
    [
        [15,13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7,10,11]
    ]

## Solution

### Solution I: Recursion
In each recursion, we rotate the outer shell of the given matrix firstly; then, come to the subproblem, rotating the inner image/matrix (matrix[1:-1, 1:-1]) whcih can be taken as the next recursion.

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) <= 1:
            return
        
        start, end, length = 0, len(matrix) - 1, len(matrix)
        while end > start:
            for i in range(end - start):
                (matrix[start][start+i], matrix[start+i][end],
                 matrix[end][end-i], matrix[end-i][start]) =(
                 matrix[end-i][start], matrix[start][start+i],
                 matrix[start+i][end], matrix[end][end-i])
                
            start += 1
            end -= 1
        
        return
```

