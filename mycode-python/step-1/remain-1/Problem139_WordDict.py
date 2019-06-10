class Solution(object):
    def wordBreak(self, s, wordDict):
        len_s = len(s)
        dp = [0] * (len_s+1)
        dp[0] = 1
        for i in range(1,len_s+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = 1
                    break
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print s.wordBreak('leetcode',['leet','code'])