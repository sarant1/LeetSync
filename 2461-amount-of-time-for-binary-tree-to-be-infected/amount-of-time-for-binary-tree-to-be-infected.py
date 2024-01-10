# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft() 
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    q.append(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    q.append(node.right)
        visited = set([start])
        q = deque([start])
        time = -1
        while q:
            time+=1
            for _ in range(len(q)):
                cur = q.popleft()
                visited.add(cur)
                for val in graph[cur]:
                    if val not in visited:
                        q.append(val)
        return time


            


        
        