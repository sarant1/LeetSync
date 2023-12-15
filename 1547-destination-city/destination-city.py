class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest = set()
        start = set()
        for i in range(len(paths)):
            start.add(paths[i][0])
            dest.add(paths[i][1])
        for i in range(len(paths)):
            if paths[i][1] not in start:
                return paths[i][1]
        return ""
            
        