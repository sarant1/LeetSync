# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        lengthOfParts = count // k
        remainder = count % k

        curr = head
        ans = []

        for i in range(k):
            ans.append(curr)
            for j in range(lengthOfParts-1 + (1 if remainder else 0)):
                if not curr: break
                curr = curr.next
            remainder -= (1 if remainder else 0)

            if curr:
                curr.next, curr = None, curr.next
        
        return ans

