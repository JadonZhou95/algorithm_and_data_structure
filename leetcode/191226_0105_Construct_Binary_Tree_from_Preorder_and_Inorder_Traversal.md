# Construct Binary Tree from Preorder and Inorder Traversal

## Problem
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:

        3
       / \
      9  20
      /  \
     15   7

## Solution

### Recursion
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        value = preorder[0]
        node = TreeNode(value)
        if len(preorder) == 1:
            return node
        
        index = inorder.index(value)
        left_child = self.buildTree(preorder[1:1+index], inorder[0:index])
        right_child = self.buildTree(preorder[1+index:], inorder[index+1:])
        node.left = left_child
        node.right = right_child
        
        return node
```



