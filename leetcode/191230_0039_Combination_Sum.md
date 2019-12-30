# Combination Sum

## Problem
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

### Example 1:

    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
    [7],
    [2,2,3]
    ]

## Solution
### Recursion + Backtracking
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # important
        ans = []
        def combineSum(candidates, target, solution=[]):
            if target == 0:
                ans.append(solution)
                return
            
            for i, cand in enumerate(candidates):
                if target - cand >= 0:
                    combineSum(candidates[i:], target - cand, solution + [cand])
                else:
                    break # combine with the sort step, which avoid many abvious mistakes and improve the efficiency
            return
        
        combineSum(candidates, target)
        
        return ans
```

Efficiency:
* Time = O(num of ans)
* Memory = O(num of ans)
