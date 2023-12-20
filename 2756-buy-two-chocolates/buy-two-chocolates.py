class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        m = money
        f, s = float('inf'), float('inf')
        for num in prices:
            if num < f and num < s:
                s, f = f, num 
            elif num < s:
                s = num
        m-=f 
        m-=s
        return m if m >= 0 else money
        