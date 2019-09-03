class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i] += dp[i-1] * dp[i-j]
        return dp[-1]
if __name__ == "__main__":
    s = Solution()
    s.numTrees()