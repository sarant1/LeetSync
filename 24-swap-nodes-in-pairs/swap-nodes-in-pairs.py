# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode()
        prev = head
        if head.next:
            head = head.next
        dummy.next = head
        last = None
        if head.next and not head.next.next:
            last = head.next
            last.next = None
        while head.next and head.next.next:
            temp = head.next
            prev.next = head.next.next
            head.next = prev
            prev = temp
            head = prev.next
            if head.next and not head.next.next:
                last = head.next
                last.next = None
        head.next = prev 
        prev.next = None
        if last:
            prev.next = last 
        return dummy.next

        