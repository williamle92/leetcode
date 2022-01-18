"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def l(self, val):
        self.left = TreeNode(val)
        return self.left
    def r(self, val):
        self.right = TreeNode(val)
        return self.right


class Solution:
    def leafSimilar(self, root1, root2):
        return self.dfs(root1) == self.dfs(root2)
#   we are going to depth first search the branch 
    def dfs(self,root):
        if root.left is None and root.right is None:
            return [root.val]

        if root.left and root.right:
            return self.dfs(root.left) + self.dfs(root.right)
        
        if root.right:
            return self.dfs(root.right)
        if root.left:
            return self.dfs(root.left)
        
tree = TreeNode(1)
l_tree =tree.l(2)
l_tree.l(3)
r_tree = tree.r(3)
r_tree.l(2)
r_tree.r(4)

tree2 = TreeNode(1)
tree2.l(3)
r_tree2 = tree2.r(2)
r_tree2.l(2)
r_tree2.r(4)

s = Solution()
print(s.leafSimilar(tree, tree2))