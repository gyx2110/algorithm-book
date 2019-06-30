class Solution(object):
    def isMatch(self, s, p):
        m = len(s)+1
        n = len(p)+1
        dp = [[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(1,n):
            if p[i-1]=='*':
                dp[0][i] = 1
            else:break
        print dp[0]
        for i in range(1,m):
            for j in range(1,n):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]
if __name__ == "__main__":
    s = Solution()
    print s.isMatch('aa','*e')