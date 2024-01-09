# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            cur = "" 
            if not node.left and not node.right:
                return (str(node.val) + ",")
            if node.left:
                cur += (str(dfs(node.left)))
            if node.right:
                cur += (str(dfs(node.right)))
            return cur
        return dfs(root1) == dfs(root2) 
        