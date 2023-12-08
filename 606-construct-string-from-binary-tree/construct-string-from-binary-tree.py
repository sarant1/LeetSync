# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(cur):
            if not cur:
                return ""
            elif cur.right:
                return str(cur.val) + "(" + dfs(cur.left) + ")(" + dfs(cur.right) + ")"
            elif cur.left:
                return str(cur.val) + "(" +  dfs(cur.left) + ")"
            return str(cur.val)
        return dfs(root)
        
            


                
        return ans


        