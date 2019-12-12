# Maximum Subarray

## Problem
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

### Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

## Solution

### Solution I: 2D Dynamic Programming
For the problem that identify a substring or subarray that satisfies some requirement, it can always be solved with dynamic programming by constructing a 2D tables. Each element in the table represent a substring or subarray.

Complexity:
* Time: O(n^2)
* Memory: O(n^2)

### Solution  II: Linear Dynamic Programming
Need some observations in the problem: Scan the array, and only positive num will add on to the max sum.
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -float('Inf')
        sub_sum = 0
        
        for num in nums:
            sub_sum += num
            result = max(sub_sum, result)
            if sub_sum < 0:
                sub_sum = 0
                
        return result
```
Complexity:
* Time: O(n)
* Memory: O(1)
