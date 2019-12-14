# Subsets II

## Problem
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

### Example:

    Input: [1,2,2]
    Output:
    [
    [2],
    [1],
    [1,2,2],
    [2,2],
    [1,2],
    []
    ]

## Solution:

### Solution I: Hash Tables & Recursion
Add newly created tuples to the hash tables to avoid duplicated adding.
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def getSubSets(nums, sets):
            if not nums:
                sets.add(tuple())
                return
            
            value = nums[-1]
            getSubSets(nums[:-1], sets)
            new_sets = sets.copy()
            for subset in new_sets:
                sets.add(tuple(sorted(subset + (value,))))
            
            return
        
        sets = set([])
        getSubSets(nums, sets)

        return list(sets)
```

Complexity:
* Time: O(n^2)
* Memory: O(n^2)