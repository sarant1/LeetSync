# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, root.val, root.val)])
        ans = 0
        while q:
            cur, hi, lo = q.popleft()
            ans = max(ans, cur.val-lo, hi-cur.val)
            maxVal = max(hi, cur.val)
            minVal = min(lo, cur.val)
            if cur.left:
                q.append((cur.left, maxVal, minVal))
            if cur.right:
                q.append((cur.right, maxVal, minVal))
        return ans
            
            
        
        
            



        