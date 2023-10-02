class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        l = 0
        for r in range(len(colors)):
            if colors[l] != colors[r]:
                l = r
            curr = r - l + 1 - 2
            if curr > 0:
                if colors[r] == "A":
                    alice += 1
                if colors[r] == "B":
                    alice -= 1
        return alice > 0 
            



        