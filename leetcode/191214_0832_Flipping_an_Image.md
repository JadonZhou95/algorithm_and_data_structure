# Flipping an Image

## Problem
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

### Example 1:

    Input: [[1,1,0],[1,0,1],[0,0,0]]
    Output: [[1,0,0],[0,1,0],[1,1,1]]
    Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
    Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

## Solution
Loop through the image
```python
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for array in A:
            start, end = 0, len(array) - 1
            while end >= start:
                if end != start:
                    array[start], array[end] = array[end], array[start]
                    array[start] = (array[start] + 1) % 2
                    array[end] = (array[end] + 1) % 2
                else:
                    array[start] = (array[start] + 1) % 2
                start += 1
                end -= 1
                
        return A
```