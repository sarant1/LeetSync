class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = [1, 1]
        cur_row = []
        for i in range(1, rowIndex):
            for g in range(len(prev_row)+1):
                t = 0
                if g == 0 or g == len(prev_row):
                    t = 1
                else:
                    t = prev_row[g] + prev_row[g-1]
                cur_row.append(t)
            prev_row = cur_row
            cur_row = []
        return prev_row if rowIndex > 0 else [1]
                






        