class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        ans = []
        for course in prerequisites:
            adj[course[1]].append(course[0])
            inDegree[course[0]]+=1
        for i in range(numCourses):
            if inDegree[i] == 0:
                visited = set()
                stack = [i]
                while stack:
                    cur = stack.pop()
                    for course in adj[cur]:
                        inDegree[course]-=1
                        if inDegree[course] == 0:
                            stack.append(course)
                    if cur in visited:
                        return []
                    elif inDegree[cur] == 0:
                        ans.append(cur)
                        inDegree[cur]-=1
        return ans if len(ans) == numCourses else []


        




        