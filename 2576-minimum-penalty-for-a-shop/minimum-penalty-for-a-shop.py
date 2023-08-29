class Solution:
    def bestClosingTime(self, customers: str) -> int:
        count = 0
        if len(customers) == 2 and customers[0] == "Y" and customers[1] == "N":
            count = 1
        dp = [0 for _ in range(len(customers))]
        currMax = [0, count] # location and value
        isPos = False
        

        for i in range(len(customers)):
            if customers[i] == "Y":
                count += 1
                if count > 0:
                    isPos = True
            elif customers[i] == "N":
                count -= 1
            dp[i] = count
            if 0 <= i < len(customers) and dp[i] > currMax[1]:
                currMax[0] = i
                currMax[1] = dp[i]
        return currMax[0] + 1 if isPos else 0 











