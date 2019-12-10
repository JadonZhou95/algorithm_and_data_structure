# Remove Nth Node From End of List

## Problem
Given a linked list, remove the n-th node from the end of list and return its head.

### Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

## Solution

### Solution I: Two passes

First, find the algorithm length L, then find the L-n node and remove it.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 1
        node = head
        while node.next:
            node = node.next
            length += 1
        
        if length - n == 0:
            head = head.next if head.next else None
        else:
            node = head
            for i in range(length - n - 1):
                node = node.next
            node.next = node.next.next if node.next.next else None
        return head
```

Complexity:
* Time: O(2L - n)
* Memory: O(1)

### Solution II: One pass
Use two pointers, one is the (n-1)th node before another.

* Time: O(L)
* Memory: O(1)

## Feedback
1. Compensate some memory for less iterations or operations
2. Actually, the total number of assignments for the two algorithms are the same.
3. One-pass algorithm shows some idea of **greedy algorithms**.
