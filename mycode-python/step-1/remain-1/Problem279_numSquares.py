class Solution(object):
    def numSquares(self, n):
        if n<=1:
            return n
        dp = [_ for _ in range(0,n+1)]
        import math
        for i in range(1,n+1):
            j = int(math.sqrt(i))
            while j>=0:
                dp[i] = min(dp[i],dp[i-j*j]+1)
                j-=1
            # j = 1
            # while j*j<=i:
            #     dp[i] = min(dp[i],dp[i-j*j]+1)
            #     j+=1
        return dp[-1]
if __name__ == "__main__":
    s = Solution()
    print s.numSquares(12)

