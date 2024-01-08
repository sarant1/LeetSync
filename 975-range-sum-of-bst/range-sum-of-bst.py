# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = deque() 
        stack.append(root)
        ans = 0
        while stack:
            cur = stack.popleft()
            if cur.val >= low and cur.val <= high:
                ans+=cur.val
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return ans
        