# Longest Word in Dictionary

## Problem
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

### Example 1:

    Input: 
    words = ["w","wo","wor","worl", "world"]
    Output: "world"
    Explanation: 
    The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

### Example 2:

    Input: 
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    Output: "apple"
    Explanation: 
    Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

## Solution

### Solution I: Two Hash Tables & Recursion
```python
class Solution:
    def longestWord(self, words: List[str]) -> str:
        length, result = 0, None
        words = set(words)
        good_words = set([])
        
        for word in words:
            if len(word) >= length and self.check_exitence(word, words, good_words):
                if len(word) > length:
                    length = len(word)
                    result = word
                else:
                    result = word if word < result else result
    
        return result
                
            
    def check_exitence(self, word, words, good_words):
        if not len(word):
            return True
        
        if word in good_words:
            return True
        
        if word in words:
            if self.check_exitence(word[:-1], words, good_words):
                good_words.add(word)
                return True
        
        return False
```