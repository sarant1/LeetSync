# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(cur):
            ans = cur.val if cur.val >= low and cur.val <= high else 0 
            if cur.left:
                ans += dfs(cur.left)
            if cur.right:
                ans += dfs(cur.right)
            return ans
        return dfs(root)
        