# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node):
            nonlocal result

            if not node:
                return 0, 0
            
            left_sum, left_amt = dfs(node.left)
            right_sum, right_amt = dfs(node.right)

            cur_sum = node.val + left_sum + right_sum
            cur_total = 1 + left_amt + right_amt

            if cur_sum // cur_total == node.val:
                result += 1
            
            return cur_sum, cur_total
        dfs(root)
        return result
            
        
        