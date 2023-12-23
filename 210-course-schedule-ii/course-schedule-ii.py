class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        ans = []
        for course in prerequisites:
            adj[course[1]].append(course[0])
            inDegree[course[0]]+=1
        for i in range(len(adj)):
            if not inDegree[i]:
                stack = [i]
                visited = set() 
                while stack:
                    cur = stack.pop()
                    for crse in adj[cur]:
                        inDegree[crse]-=1
                        if not inDegree[crse]:
                            stack.append(crse)
                    if cur in visited:
                        return []
                    elif inDegree[cur] == 0:
                        inDegree[cur]-=1
                        ans.append(cur) 
                        visited.add(cur)
        return ans if len(ans) == numCourses else [] 




        