# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, cur):
            if not node:
                return
            if not node.left and not node.right:
                cur.append(node.val)
            if node.left:
                dfs(node.left, cur)
            if node.right:
                dfs(node.right, cur)
            return cur
        return dfs(root1, []) == dfs(root2, []) 
        