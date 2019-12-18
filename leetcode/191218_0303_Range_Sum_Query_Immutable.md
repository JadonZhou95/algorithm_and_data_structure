# Range Sum Query Immutable

## Problem
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

### Example:

    Given nums = [-2, 0, 3, -5, 2, -1]

    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3

## Solution

### I. Dynamic Programming(Caching)
Build a 2-D table, which contains the answers of all the ranges. Then achieve the sum range in linear time.

Complexity:
* Init: O(n^2), O(n^2)
* Get: O(1), O(1)

### II. Sum Deduction
Key Ideas: sumRange(i,j) = sum(0:j) - sum(0:i-1)

```python
class NumArray:

    def __init__(self, nums: List[int]):
        sum_value = 0
        self.sums = []
        for num in nums:
            sum_value += num
            self.sums.append(sum_value)

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j] - (self.sums[i-1] if i != 0 else 0)
```
Complexity:
* Init: O(n), O(n)
* Get: O(1), O(1)

