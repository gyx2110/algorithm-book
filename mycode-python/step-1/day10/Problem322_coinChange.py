class Solution(object):
    def coinChange(self, coins, amount):
        dp = [[-1] * (amount+1) for _ in range(len(coins)]
        while i*coins[0]<len(dp[0]):
            dp[0][i*coins[0]] = i
            i+=1
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if j>coins[i]>=0
