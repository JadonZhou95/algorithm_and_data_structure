 # Sudoku Solver
 ## Problem
 Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.

![Sudoku_puzzel](../images/Sudoku_puzzle.png)
![Sudoku_solution](../images/Sudoku_solution.png)

## Solution
### Solution I: Brutal Force
Go through every possible values for each box until find the correct one.

```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    keys = self.findKeys(board, i, j)
                    if not keys:
                        return False
                    for key in keys:
                        board[i][j] = key
                        if self.solveSudoku(board):
                            return True
                    board[i][j] = "."
                    return False
        return True

    
    def findKeys(self, board, i, j):
        """
        Find the possible keys of the required position
        """
        keys = set(list("123456789"))
        for k in range(9):
            if board[i][k] != ".":
                keys.discard(board[i][k])
            if board[k][j] != ".":
                keys.discard(board[k][j])
        
        start, end = i // 3, j // 3
        for m in range(3):
            for n in range(3):
                value = board[start*3+m][end*3+n]
                if value != ".":
                    keys.discard(value)
        
        return list(keys)
```
Complexity:
* Time: O(n^10)?
* Memory: O(1)
