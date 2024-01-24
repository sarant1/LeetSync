# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def can_palindrome(cur_count):
            loner = False
            for count in cur_count:
                if count % 2 == 0:
                    continue
                elif count == 1 and loner == False:
                    loner = True
                elif count % 2 and loner == False:
                    loner = True
                else:
                    return 0
            return 1
        def dfs(node, cur_count):
            ans = 0
            cur_count[node.val]+=1
            if not node.left and not node.right:
                temp = can_palindrome(cur_count)
                cur_count[node.val]-=1
                return temp
            if node.left:
                ans += dfs(node.left, cur_count)
            if node.right:
                ans += dfs(node.right, cur_count)
            cur_count[node.val]-=1
            return ans
        counts = [0] * 10
        return dfs(root, counts)
        