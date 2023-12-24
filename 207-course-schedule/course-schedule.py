class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for course in prerequisites:
            adj[course[1]].append(course[0])
            inDegree[course[0]]+=1
        stack = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                stack.append(i)
        while stack:
            cur = stack.pop()
            for course in adj[cur]:
                inDegree[course]-=1
                if inDegree[course] == 0:
                    stack.append(course)
        return all(inD==0 for inD in inDegree)
        

        