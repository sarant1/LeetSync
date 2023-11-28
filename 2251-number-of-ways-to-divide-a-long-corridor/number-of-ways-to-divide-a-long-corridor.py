class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7
        l, r, count, ans, total_s = 0, 0, 0, 1, 0
        while r < len(corridor):
            if count == 2:
                while r < len(corridor) and corridor[r] == "P":
                    r+=1
                if r >= len(corridor):
                    break
                if r != l:
                    ans*=(r-l+1)
                l = r
                count = 0
            elif corridor[r] == "S":
                total_s+=1
                count+=1
                l+=1
                r+=1
            else:
                r+=1
                l+=1
        if total_s % 2 != 0 or total_s == 0:
            return 0
        return ans % mod 





        