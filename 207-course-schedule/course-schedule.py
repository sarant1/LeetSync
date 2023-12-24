class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        inDegrees = [0] * numCourses
        for course in prerequisites:
            adj[course[1]].append(course[0])
            inDegrees[course[0]]+=1
        stack = []
        for i in range(numCourses):
            if inDegrees[i] == 0:
                stack.append(i)
        while stack:
            cur = stack.pop()
            for course in adj[cur]:
                inDegrees[course]-=1
                if inDegrees[course] == 0:
                    stack.append(course)
        return all(inDegree == 0 for inDegree in inDegrees)
        

        