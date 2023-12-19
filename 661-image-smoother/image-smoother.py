class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def get_average(x, y):
            total, amt = 0, 0
            dirs = [[0, 1],[0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1], [0, 0]] 
            for m, n in dirs:
                j, k = x + m, y + n
                if j >= 0 and j < len(img) and k >=0 and k < len(img[j]):
                    amt+=1
                    total+=img[j][k]
            return total // amt 
        ans = []
        for i in range(len(img)):
            ans.append([])
            for j in range(len(img[i])):
                ans[i].append(get_average(i, j))
        return ans

        