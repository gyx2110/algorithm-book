class Solution(object):
    def longestPalindrome(self, s):
        length = len(s)
        if length < 2:
            return '' if length==0 else s
        dp = [[0] * length for i in range(length)]
        start = 0
        end = 0
        # 枚举子串的长度
        for l in range(1,length+1):
            low = 0
            while low+l-1 < length:
                high = low + l -1
                if s[low] == s[high] and (high-low<=1 or dp[low+1][high-1]):
                    dp[low][high] = 1
                    start = low
                    end = high
                low+=1
        return s[start:end+1]
if __name__ == "__main__":
    s = Solution()
    print s.longestPalindrome('babad')