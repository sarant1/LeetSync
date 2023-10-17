class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n


        for i in range(n):
            left, right = leftChild[i], rightChild[i]
            if left != -1:
                indegree[left] += 1
            if right != -1:
                indegree[right] += 1
        root = None
        for i in range(len(indegree)):
            if indegree[i] == 0:
                if not root:
                    root = i 
                else:
                    return False
            elif indegree[i] > 1:
                return False
        if root is None:
            return False
        queue = deque([root])
        visited = [False] * n
        while queue:
            cur = queue.popleft()
            visited[cur] = True
            if leftChild[cur] != -1:
                queue.append(leftChild[cur]) 
            if rightChild[cur] != -1:
                queue.append(rightChild[cur])
        return sum(visited) == n










        