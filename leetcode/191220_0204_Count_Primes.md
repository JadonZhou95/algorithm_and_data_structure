# Count Primes

## Problem
Count the number of prime numbers less than a non-negative number, n.

### Example:

    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

## Solution
### I. Sieve of Eratosthenes 
Starts from small numbers to find its multiplier smaller than the input x.
```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n in [0,1,2]:
            return 0
        
        nums = [True] * n
        
        for num in range(2, n // 2 + 1):
            if nums[num]:
                for numb in range(num, n):
                    value = num * numb
                    if value < n:
                        nums[value] = False
                    else:
                        break
                        
        return sum(nums) - 2
```


