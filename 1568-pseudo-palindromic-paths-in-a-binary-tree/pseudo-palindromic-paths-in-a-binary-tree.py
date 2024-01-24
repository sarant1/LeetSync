# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = [0] * 10
        def can_palindrome(cur_count):
            odd = 0
            for cnt in cur_count:
                if cnt % 2:
                    odd+=1
            return 1 if odd <= 1 else 0
        def dfs(node, cur_count):
            ans = 0
            if not node:
                return 0
            cur_count[node.val]+=1
            if not node.left and not node.right:
                temp = can_palindrome(cur_count)
                cur_count[node.val]-=1
                return temp
            ans += dfs(node.left, cur_count)
            ans += dfs(node.right, cur_count)
            cur_count[node.val]-=1
            return ans

        return dfs(root, count)
        