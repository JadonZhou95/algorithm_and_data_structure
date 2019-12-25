# Symmetric Tree

## Problem
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3

## Solution

I. Recursion
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def compare(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is not None and node2 is not None:
                if node1.val == node2.val:
                    return (compare(node1.left, node2.right) and
                           compare(node1.right, node2.left))
                else:
                    return False
            else:
                return False
            
        if not root:
            return True
        
        return compare(root.left, root.right)
```

Complexity:
* Time: O(n)
* Memory:O(1)