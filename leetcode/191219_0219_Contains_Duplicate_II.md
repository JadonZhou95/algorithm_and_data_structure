# Contains Duplicate II

## Problem
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

### Example 1:

    Input: nums = [1,2,3,1], k = 3
    Output: true

### Example 2:

    Input: nums = [1,0,1,1], k = 1
    Output: true

## Solution

I. Hash Tables
```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_pos = dict()
        for i, num in enumerate(nums):
            if num not in num_pos:
                num_pos[num] = i
                continue
            
            if i - num_pos[num] <= k:
                return True

            num_pos[num] = i
            
        return False
```

Complexity
* Time: O(n)
* Memory: O(n)
