# Letter Combinations of a Phone Number

## Problem
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![Phone-keypads](../images/Telephone-keypad.png)

### Example:

    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Solution

### I. Recursion and hash table
```python
class Solution:
    num_chars = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno",\
                "7":"pqrs", "8":"tuv", "9":"wxyz"}
    
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        results = []
        subs = self.letterCombinations(digits[1:])
        if not subs:
            subs.append("")
        for char in list(self.num_chars[digits[0]]):
            for sub in subs:
                results.append(char + sub)
                
        return results
```
Complexity
* Time: O(k^n)
* Memory: O(k^n)
