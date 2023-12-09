# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        visited = set() 
        def dfs(cur):
            if cur.left:
                dfs(cur.left)
            ans.append(cur.val)
            if cur.right:
                dfs(cur.right)
        dfs(root)
        return ans
            

        
        