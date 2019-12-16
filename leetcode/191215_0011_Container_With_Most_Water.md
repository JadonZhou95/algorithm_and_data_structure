# Container With Most Water

## Problem
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
![container with most water](../images/container_with_most_water.jpg)

### Example:

    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49

## Solution
### Solution I: Brute Force
Try every combination of sides and find the max water.
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_value = 0
        for i, h_start in enumerate(height):
            for j, h_end in enumerate(height[i:]):
                water = (j) * min(h_start, h_end)
                max_value = max(water, max_value)
        
        return max_value
```
Complexity:
Time: O(n^2)
Memory: O(1)

### Solution II: Shrink from the Short Side
This solution needs some observation to find out. Basically, every time the max water computed and compared is larger than all other combination of water sides of which using the short side.
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right, gap = 0, len(height) -1, len(height) - 1
        while gap > 0:
            # max_water = max(max_water, min(height[left], height[right]) * gap)
            if height[left] > height[right]:
                min_side = height[right]
                right -= 1
            else:
                min_side = height[left]
                left += 1
            max_water = max(max_water, min_side * gap)
            gap -= 1
        
        return max_water
```

