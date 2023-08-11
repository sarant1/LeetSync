class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)] 
        visitSet = set()

        for pair in prerequisites:
            adj[pair[1]].append(pair[0])
        
        def dfs(i):
            if i in visitSet:
                return False
            if len(adj[i]) == 0:
                return True
            visitSet.add(i)
            for pre in adj[i]:
                if not dfs(pre): return False
            visitSet.remove(i)
            adj[i] = [] 
            return True
        for course in range(1, numCourses):
            if not dfs(course): return False
        return True






            

        

                
            
            
            






