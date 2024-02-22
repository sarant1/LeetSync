class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        elif not trust:
            return -1
        trusting = [0] * (n + 1)
        checked = set() 
        judge = -1
        for boy in trust:
            trusting[boy[1]]+=1
            checked.add(boy[0])
        cur = -1
        for i in range(len(trusting)):
            if trusting[i] > cur:
                cur = trusting[i]
                judge = i
        return judge if judge not in checked and len(checked) + 1 == n else -1

        