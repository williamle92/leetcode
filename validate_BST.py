"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root) -> bool:
#       creating a list with a tuple of root, and arbitary upper and lower limits
#       DFS
        stack = [(root, -float("inf"), float('inf'))]
        
        while len(stack):
#           splitting the the tuple into three values, which is the node which it is at, the minimum bound to compare, and upper bound to compare
#           Later we are going to substitute depending on the left or right, where what becomes the low or upper bound
            node, low_bound, upper_bound = stack.pop()
#           Checking at each level to see if the value is greater than the left side, and the value less then the right side. 
            if node.val <= low_bound or node.val >= upper_bound:
                return False
#           Traversing the left branch now: if there is a node.left value, we append it to the tuple
            if node.left:
                stack.append((node.left, low_bound, node.val))
            
            if node.right:
                stack.append((node.right, node.val, upper_bound))
                
        return True
#       Solution solved with O(n) time and space