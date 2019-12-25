# Longest Harmonious Subsequence

## Problem
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

### Example 1:

    Input: [1,3,2,2,5,2,3,7]
    Output: 5
    Explanation: The longest harmonious subsequence is [3,2,2,2,3].

## Solution

### I. One Pass Hash Table
```python
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = dict()
        result = 0
        for num in nums:
            counts[num] = counts[num] + 1 if num in counts else 1
            if num - 1 in counts:
                result = max(result, counts[num - 1] + counts[num])
            if num + 1 in counts:
                result = max(result, counts[num + 1] + counts[num])
        
        return result
```

Complexity
* Time: O(n)
* Memory: O(n)