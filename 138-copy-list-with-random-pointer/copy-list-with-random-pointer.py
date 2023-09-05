"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hmap = {}
        while curr:
            hmap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            if curr.random:
                hmap[curr].random = hmap[curr.random]
            if curr.next:
                hmap[curr].next = hmap[curr.next]
            curr = curr.next

        return hmap[head] if head else None 
    
        

        
