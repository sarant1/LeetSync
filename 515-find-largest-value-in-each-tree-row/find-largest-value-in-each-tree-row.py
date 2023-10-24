# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            cur_max = float('-inf')
            cur_row = []
            for node in q:
                cur_max = max(cur_max, node.val)
                if node.left:
                    cur_row.append(node.left)
                if node.right:
                    cur_row.append(node.right)
            q = cur_row
            ans.append(cur_max)
        return ans


        

        
        