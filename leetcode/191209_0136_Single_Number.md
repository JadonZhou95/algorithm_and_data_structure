# Single Number
## Problem
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

    Input: [2,2,1]
    Output: 1

Example 2:

    Input: [4,1,2,1,2]
    Output: 4

## Solution

### Solution I: Hash Tables
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_sets = set([])
        for num in nums:
            if num in num_sets:
                num_sets.remove(num)
            else:
                num_sets.add(num)
        
        return num_sets.pop()
```
Complexity:
* Time: O(n)
* Memory: O(n)

### Solution II: Bit operation
#### Concept

If we take XOR of zero and some bit, it will return that bit
    
    a⊕0=a

If we take XOR of two same bits, it will return 0
        
    a⊕a=0

a⊕b⊕a=(a⊕a)⊕b=0⊕b=b

So we can XOR all bits together to find the unique number.

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
```

#### Complexity

* Time: O(n)
* Space: O(1)


