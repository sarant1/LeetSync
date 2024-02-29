# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even = True
        cur_row = [root]
        while cur_row:
            even = not even
            next_row = []
            cur_val = None
            for node in cur_row:
                if (even and node.val % 2 != 0 ) or (even and cur_val and node.val >= cur_val):
                    return False
                elif (not even and node.val % 2 != 1) or (not even and cur_val and node.val <= cur_val):
                    return False
                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)
                cur_val = node.val
            cur_row = next_row

        return True 