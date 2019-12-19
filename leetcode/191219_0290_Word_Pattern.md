# Word Pattern

## Problem
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

### Example 1:

    Input: pattern = "abba", str = "dog cat cat dog"
    Output: true

### Example 2:

    Input:pattern = "abba", str = "dog cat cat fish"
    Output: false

## Solution
### I. Hash Tables
```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        char_word = dict()
        cache = set([])     
        words = str.split()
        
        if len(pattern) != len(words):
            return False

        for char, word in zip(pattern, words):
            if char not in char_word:
                if word in cache:
                    return False
                char_word[char] = word
                cache.add(word)
            else:
                if char_word[char] != word:
                    return False
        
        return True
```
Complexity
* Time:O(n)
* Memory:O(n)