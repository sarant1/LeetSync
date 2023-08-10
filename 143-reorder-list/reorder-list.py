# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head.next or not head.next.next:
            return 
        
        slow = head
        fast = head.next

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        if fast.next:
            fast = fast.next 
        
        prev = slow
        curr = slow.next
        stack = []
        stack.append(prev)

        while curr.next:
            stack.append(curr)
            curr = curr.next
        stack.append(curr)

        h2 = head 
        while stack:
            temp = h2.next
            h2.next = stack.pop()
            h2.next.next = temp
            h2 = temp
        slow.next = None 





