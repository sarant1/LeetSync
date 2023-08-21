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
        if not head:
            return None
        hmap = {}
        q = deque()

        prev = head
        curr = prev.next
        while curr:
            hmap[prev] = Node(prev.val, None, None)
            q.append((hmap[prev],prev.random, prev.next))
            prev = curr
            curr = curr.next
        hmap[prev] = Node(prev.val, None, None)
        q.append((hmap[prev], prev.random, prev.next))
        while q:
            curr, rand, nextNode = q.popleft()
            if nextNode:
                curr.next = hmap[nextNode]
            if rand:
                curr.random = hmap[rand]
            else:
                curr.random = None
        return hmap[head]

        
