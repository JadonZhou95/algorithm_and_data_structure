# Bulls and Cows

## Problem
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

### Example 1:

    Input: secret = "1807", guess = "7810"

    Output: "1A3B"

    Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

## Solution

I. One pass & Direct addressing
```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        
        sec = [0 for i in range(10)]
        gue = sec[:]
        
        for s_char, g_char in zip(secret, guess):
            if s_char == g_char:
                bulls += 1
            else:
                s_val, g_val = int(s_char), int(g_char)
                if sec[g_val]:
                    sec[g_val] -= 1
                    cows += 1
                else:
                    gue[g_val] += 1
                    
                if gue[s_val]:
                    gue[s_val] -= 1
                    cows += 1
                else:
                    sec[s_val] += 1
        
        return "{}A{}B".format(bulls, cows)
```
Complexity
* Time: O(n)
* Memory: O(1)