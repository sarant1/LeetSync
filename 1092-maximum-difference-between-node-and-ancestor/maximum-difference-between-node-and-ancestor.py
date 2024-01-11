# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, maxVal, minVal, ans):
            if not node:
                return 0
            maxVal = max(node.val, maxVal)
            minVal = min(node.val, minVal)
            diff1 = max(ans, dfs(node.left,maxVal, minVal, ans))
            diff2 = max(ans, dfs(node.right,maxVal, minVal, ans))
            currdiff = max(diff1, diff2)
            return max(ans, node.val-minVal, maxVal-node.val, currdiff)
        return dfs(root, root.val, root.val, 0)
            
            
        
        
            



        