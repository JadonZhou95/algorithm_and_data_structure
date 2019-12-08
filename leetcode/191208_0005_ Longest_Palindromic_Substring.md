#  Longest Palindromic Substring

## Problems
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

### Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

### Example 2:

    Input: "cbbd"
    Output: "bb"

## Solutions:
### Solution I: Dynamic Programming
Based on that idea that if S is a palindromic, then:
1. S[1:-1] must be  a palindromic, and
2. S[0] == S[-1]

In order to compare all the cases involoved, a **2D table** is constructed.
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        table = [[True] * len(s)  for i in range(len(s))]
        a, b = 0, 0
        for length in range(1, len(s) + 1):
            if length == 1:
                continue
            
            j = length - 1
            update = True
            for i in range(len(s) - j):
                table[i][i + j] = (table[i + 1][i + j - 1] and 
                                   s[i] == s[i + j])
                if update and table[i][i + j]:
                    update = False
                    a, b = i, i + j
        
        return s[a:b+1]  
```

Complexcity: 
* Time: O(n^2)
* MEmory: O(n^2)

### Solution II: Expend Around Center
Each single element or element pair with the same char can be taken as the center of the palindromics. By comparing the front and back element, the palindromics can be expended and the comparison can continue.
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length, start, end = 0, 0, 0
        for i, char in enumerate(s):
            for k in [1, 2]:
                s_start, s_end = i, i + k
                while True:
                    if self.checkPalindrome(s, s_start, s_end - 1):
                        s_length = s_end - s_start
                        if s_length > length:
                            length, start, end = s_length, s_start, s_end
                        s_start -= 1
                        s_end += 1
                    else:
                        break         
        return s[start: end]
                
        
        
    def checkPalindrome(self, s, start, end):
        if start >= 0 and end < len(s) and s[start] == s[end]:
            return True
        return False
```
Complexcity
* Time: O(n^2)
* Memory: O(1)

### Solution III: Manacher’s Algorithm
To be studied: 
[Manacher’s Algorithm – Linear Time Longest Palindromic Substring](https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/)
