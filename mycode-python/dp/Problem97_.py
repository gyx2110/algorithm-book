class Solution(object):
    def isInterleave(self, s1, s2, s3):
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len(s3) != len_s1+len_s2:
            return False
        if "" == s3:
            return True
        n = len_s1 + 1
        m = len_s2 + 1
        #dp[i][j]的含义是s1[0..i)和s2[0..j)能否交错组成s3[0..i+j)
        dp = [[0]*(m) for _ in range(n)]
        dp[0][0] = 1
        for i in range(1,m):
            if s2[i-1] != s3[i-1]:
                break
            dp[0][i] = 1
        for i in range(1,n):
            if s1[i-1] != s3[i-1]:
                break
            dp[i][0] = 1
        for i in range(1,n):
            for j in range(1,m):
                if (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1]):
                    dp[i][j] = 1
        return dp[-1][-1]
if __name__ == "__main__":
    s = Solution()
    print s.isInterleave("a","","a")