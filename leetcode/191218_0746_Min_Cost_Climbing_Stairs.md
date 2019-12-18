# Min Cost Climbing Stairs

## Problem
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

### Example 1:

    Input: cost = [10, 15, 20]
    Output: 15
    Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

## Solutions:
### I. Dynamic programming
pay[i] = min(pay[i-1], pay[i-2]) + cost[i]

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 1:
            return 0
        
        step1 = cost[0]
        step2 = cost[1]
        
        for i in range(2, len(cost)):
            step1, step2 = step2, min(step1, step2) + cost[i]
            
        return min(step1, step2)
```

Complexity:
* Time: O(n)
* Memory: O(1)