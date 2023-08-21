class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        inDegrees = [0]*numCourses

        for c,p in prerequisites:
            adj[p].append(c)
            inDegrees[c]+=1

        q = deque() 
        ans = []
        visited = {i:False for i in range(numCourses)} 

        for i in range(len(inDegrees)):
            if inDegrees[i] == 0:
                q.append(i)
        while q:
            current = q.popleft()
            ans.append(current)


            for next_course in adj[current]:
                inDegrees[next_course] -= 1
                if inDegrees[next_course] == 0:
                    q.append(next_course)

        return len(ans) == numCourses






            








            

        

                
            
            
            






