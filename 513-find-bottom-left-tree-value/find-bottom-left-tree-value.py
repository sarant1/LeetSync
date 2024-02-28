# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        cur_row = [root]
        last_row = []
        while cur_row: 
            last_row = cur_row
            next_row = []
            for node in cur_row:
                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)
            cur_row = next_row
        return last_row[0].val


        