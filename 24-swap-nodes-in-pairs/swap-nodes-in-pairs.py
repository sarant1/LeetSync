# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        prev, cur, ans = None, head, head.next

        while cur and cur.next:
            adj = cur.next
            if prev:
                prev.next = adj
            adj.next, cur.next = cur, adj.next
            prev, cur = cur, cur.next
        return ans or head

            





        